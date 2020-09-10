#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: rabin_karp.py
@time: 2020/9/9 15:34
@function:

This is a Rabin-Karp(RK) algorithm implementation
Method:
1. compute the pattern string's hash H(pat)
2. iterate through all sub string in text string with length M, hashing and compare.
3. if hash value equals, compare the substring. if match, return found index.

"""
import math
import random


# The following part is borrowed from https://langui.sh/2009/03/07/generating-very-large-primes/
# in an effort to implement the missing long_random_prime() function
def _rabin_miller(n):
    s = n - 1
    t = 0
    while s & 1 == 0:
        s = int(s / 2)
        t += 1
    k = 0
    while k < 128:
        a = random.randrange(2, n - 1)
        # a^s is computationally infeasible.  we need a more intelligent approach
        # v = (a**s)%n
        # python's core math module can do modular exponentiation
        v = pow(a, s, n)  # where values are (num,exp,mod)
        if v != 1:
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % n
        k += 2
    return True


def _is_prime(n):
    # lowPrimes is all primes (sans 2, which is covered by the bitwise and operator)
    # under 1000. taking n modulo each lowPrime allows us to remove a huge chunk
    # of composite numbers from our potential pool without resorting to Rabin-Miller
    lowPrimes = [
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
        257,
        263,
        269,
        271,
        277,
        281,
        283,
        293,
        307,
        311,
        313,
        317,
        331,
        337,
        347,
        349,
        353,
        359,
        367,
        373,
        379,
        383,
        389,
        397,
        401,
        409,
        419,
        421,
        431,
        433,
        439,
        443,
        449,
        457,
        461,
        463,
        467,
        479,
        487,
        491,
        499,
        503,
        509,
        521,
        523,
        541,
        547,
        557,
        563,
        569,
        571,
        577,
        587,
        593,
        599,
        601,
        607,
        613,
        617,
        619,
        631,
        641,
        643,
        647,
        653,
        659,
        661,
        673,
        677,
        683,
        691,
        701,
        709,
        719,
        727,
        733,
        739,
        743,
        751,
        757,
        761,
        769,
        773,
        787,
        797,
        809,
        811,
        821,
        823,
        827,
        829,
        839,
        853,
        857,
        859,
        863,
        877,
        881,
        883,
        887,
        907,
        911,
        919,
        929,
        937,
        941,
        947,
        953,
        967,
        971,
        977,
        983,
        991,
        997,
    ]
    if n >= 3:
        if n & 1 != 0:
            for p in lowPrimes:
                if n == p:
                    return True
                if n % p == 0:
                    return False
            return _rabin_miller(n)
    return False


def long_random_prime(k):
    """Generates a random prime.
    :param k: the desired bit length of the prime
    :returns: a random prime of bit length k
    """
    # k is the desired bit length
    r = 100 * (math.log(k, 2) + 1)  # number of attempts max
    r_ = r
    while r > 0:
        # randrange is mersenne twister and is completely deterministic
        # unusable for serious crypto purposes
        n = random.randrange(2 ** (k - 1), 2 ** (k))
        r -= 1
        if _is_prime(n):
            return n
    return "Failure after " + r_ + " tries."


class RabinKarp:
    def __init__(self, pattern: str):
        """
        init function

        :param pattern: the pattern string to search
        :param R: the alphabet size or radix
        """
        self.pat = pattern
        # radix =ascii set size
        self.R = 256
        self.m = len(pattern)
        self.q = long_random_prime(32)
        self.RM = 1
        # compute R^m-1 mod q for use
        for i in range(self.m):
            self.RM = (self.R * self.RM) % self.q
        self.patHash = self._hash(self.pat, self.m)

    def _hash(self, key, m):
        """
        return a rabin fingerprint hash value for given key string within m length
        the formula is
        H=(c0*R^m-1+c1*R^m-2+...cm-1*R^0) mod q, q is a random large_prime
        with mode equation, (a mod n)mod n = a mod n,so each iteration can use mod to reduce hash result range
        this can be calculate through iteration
        :param key:
        :param m:
        :return:
        """
        h = 1
        for j in range(m):
            h = (h * self.m + ord(key[j])) % self.q
        return h

    def check(self, pat, txt, offset):
        for i in range(self.m):
            if pat[i] != txt[i + offset]:
                return False
        return True

    def search(self, txt):
        q = self.q
        m = self.m
        n = len(txt)
        R = self.R
        RM = self.RM
        if n < self.m:
            return n
        txtHash = self._hash(txt, m)

        if self.patHash == txtHash:
            return 0

        # i start from index=m, ending to n, the substring index start from i-M+1
        for i in range(m, n):
            # remove leading digit, adding tail digit for next substring hash
            txtHash = (txtHash + q - RM * ord(txt[i - m]) % q) % q
            txtHash = (txtHash * R + ord(i)) % q
            offset = i - m + 1
            if self.patHash == txtHash and self.check(self.pat, txt, offset):
                return offset

        # no match
        return n

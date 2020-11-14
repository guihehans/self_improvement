#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: trie_st.py
@time: 2020/9/22 14:55
@function:

a trie with symbol table implementation
"""


class TrieST:
    R = 256

    class Node:
        def __init__(self, val):
            R = 256
            self.val = val
            self.next = [None] * self.R

    def __init__(self):
        self._root = self.Node()
        # number of keys in trie
        self._n = 0

    def get(self, key):
        """

        :param key:
        :return:
        """
        x = self._get(self._root, key, 0)
        return None if x is None else x.val

    def _get(self, x: Node, key, d):
        if x is None:
            return None
        # end when len(key)=param d means all keys are read.
        if d == len(key):
            return x
        c = key[d]
        return self._get(x.next[ord(c)], key, d + 1)

    def put(self, key, val):
        if val is None:
            self.delete(key)
        else:
            self._root = self._put(self._root, key, val, 0)

    def _put(self, x, key, val, index):
        if x is None:
            x = self.Node()
        if index == len(key):
            if x.val is None:
                self._n += 1
            x.val = val
            return x
        char = key[index]
        x.next[ord(char)] = self._put(x.next[ord(char)], key, val, index + 1)
        return x

    def delete(self, key):
        self._root = self._delete(self._root, key, 0)

    def _delete(self, x: Node, key, index) -> Node:
        if x is None:
            return None
        if index == len(key):
            if x.val is not None:
                self._n -= 1
            x.val = None
        else:
            char = key[index]
            x.next[ord(char)] = self._delete(x.next[ord(char)], key, index + 1)

        # remove subtrie rooted at x if it is completely empty
        if x.val is not None:
            return x
        # if subtrie next[c] not none, return its root
        for c in range(0, self.R):
            if x.next[c] is not None:
                return x
        return None

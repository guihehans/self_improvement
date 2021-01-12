#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: frequency_stack.py
@time: 2021/1/11 17:37
@function:

"""
import collections
from heapq import *
import heapq


class FreqStack:

    def __init__(self):
        # Counter encapsulate the freq counter function. provide key not exit, it's default value to 0.
        self.freq = collections.Counter()
        # defaultdict accept a construct function(list). if key not exist, create a list as stack
        self.group = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.max_freq:
            self.max_freq = f
        self.group[f].append(x)

    def pop(self) -> int:
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        # if group [max_freq] is empty, then the max_freq no element, max_freq--.
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()


def test():
    frequencyStack = FreqStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


def test_1():
    frequencyStack = FreqStack()
    frequencyStack.push(5)
    frequencyStack.push(7)
    frequencyStack.push(5)
    frequencyStack.push(7)
    frequencyStack.push(4)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


if __name__ == '__main__':
    test()

#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: reorganize_string_k_distance.py
@time: 2021/1/11 11:16
@function:

"""
from collections import deque
from heapq import *
from typing import List


def reorganize_string_my(S: str, k: int) -> str:
    if k <= 1:
        return S
    freq_map = {}
    for char in S:
        freq_map[char] = freq_map.get(char, 0) + 1

    max_heap = []
    for char, freq in freq_map.items():
        heappush(max_heap, (-freq, char))

    result = []

    while max_heap and len(max_heap) >= k:
        result, max_heap = get_k_distinct_char(max_heap, k, result)

    if max_heap:
        for i in range(len(max_heap)):
            if max_heap:
                freq, char = heappop(max_heap)
                result.append(char)

    return "".join(result) if len(result) == len(S) else ""


def get_k_distinct_char(max_heap, k, result: List):
    tmp = []
    for i in range(k):
        if max_heap:
            freq, char = heappop(max_heap)
            freq += 1
            result.append(char)
            tmp.append([freq, char])

    for freq, char in tmp:
        if -freq > 0:
            heappush(max_heap, (freq, char))

    return result, max_heap


def validate_string(S, k):
    freq_map = {}
    if not S:
        return False
    for i in range(len(S)):
        char = S[i]
        if char not in freq_map:
            freq_map[char] = i
        else:
            if i - freq_map[char] < k:
                return False
            else:
                freq_map[char] = i
    return True


def reorganize_string(str, k):
    if k <= 1:
        return str

    charFrequencyMap = {}
    for char in str:
        charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

    maxHeap = []
    # add all characters to the max heap
    for char, frequency in charFrequencyMap.items():
        heappush(maxHeap, (-frequency, char))

    queue = deque()
    resultString = []
    while maxHeap:
        frequency, char = heappop(maxHeap)
        # append the current character to the result string and decrement its count
        resultString.append(char)
        # decrement the frequency and append to the queue
        queue.append((char, frequency + 1))
        if len(queue) == k:
            char, frequency = queue.popleft()
            if -frequency > 0:
                heappush(maxHeap, (frequency, char))

    # if we were successful in appending all the characters to the result string, return it
    return ''.join(resultString) if len(resultString) == len(str) else ""


def test():
    input = "mmpp"
    k = 2
    result = reorganize_string(input, k)
    assert validate_string(result, k) is True


def test_1():
    input = "programming"
    k = 2
    result = reorganize_string(input, k)
    assert validate_string(result, k) is True


def test_2():
    input = "aab"
    k = 2
    result = reorganize_string(input, k)
    assert validate_string(result, k) is True


def test_3():
    input = "aappa"
    k = 3
    result = reorganize_string(input, k)
    assert validate_string(result, k) is False


def test_4():
    input = "aabbcc"
    k = 3
    result = reorganize_string(input, k)
    assert validate_string(result, k) is True


def test_5():
    input = "aaadbbcc"
    k = 2
    result = reorganize_string(input, k)
    assert validate_string(result, k) is True


def test_6():
    input = "aaabc"
    k = 3
    result = reorganize_string(input, k)
    assert validate_string(result, k) is True


if __name__ == '__main__':
    test()

"""
@author: guihehans
@file: quadruple_sum_target.py
@time: 2020/11/24 23:04
@function:

"""


def search_quadruplets(arr, target):
    arr.sort()
    quadruples = []
    for i in range(len(arr)):
        # skip repeated element
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        for j in range(i + 1, len(arr)):
            # skip repeated element. not j start from i+1
            if j > i + 1 and arr[j - 1] == arr[j]:
                continue
            search_quadruple(arr, i, j, target, quadruples)

    return quadruples


def search_quadruple(arr, i, j, target, quadruples):
    left = j + 1
    right = len(arr) - 1
    while left < right:
        if arr[i] + arr[j] + arr[left] + arr[right] == target:
            quadruple = [arr[i], arr[j], arr[left], arr[right]]
            # the sort is guaranteed by i j left right sequence.
            quadruples.append(quadruple)
            left += 1
            right -= 1
            # skip repeated element
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            # skip repeated element
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif arr[i] + arr[j] + arr[left] + arr[right] < target:
            left += 1  # need bigger sum
        elif arr[i] + arr[j] + arr[left] + arr[right] > target:
            right -= 1  # need smaller sum


def test_0():
    arr = [2, 0, -1, 1, -2, 2]
    target = 2
    result = search_quadruplets(arr, target)
    print(result)
    assert [-2, 0, 2, 2] in result
    assert [-1, 0, 1, 2] in result


def test_1():
    arr = [4, 1, 2, -1, 1, -3]
    target = 1
    result = search_quadruplets(arr, target)
    print(result)
    test_result = [[-3, -1, 1, 4], [-3, 1, 1, 2]]
    for i in test_result:
        assert i in result


def test_repeat():
    arr = [2, 0, 0, -1, 1, -2, 2]
    target = 0
    result = search_quadruplets(arr, target)
    print(result)
    test_result = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    for i in test_result:
        assert i in result


def test_empty():
    arr = []
    target = 0
    result = search_quadruplets(arr, target)
    print(result)
    test_result = []
    assert test_result == result


if __name__ == '__main__':
    test_1()
    test_0()
    test_repeat()
    test_empty()

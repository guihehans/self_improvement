"""
@author: guihehans
@file: quadrulple_sum_target.py 
@time: 2020/11/24 23:04
@function:

"""


def search_quadruplets(arr, target):
    quadruplets = []
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        to_find = target - arr[i]
        triplets = search_triplet(arr, to_find, i + 1)
        if triplets:
            for tri in triplets:
                tri.append(arr[i])
                tri.sort()
                quadruplets.append(tri)
    return quadruplets


def search_triplet(arr, target, j):
    triplets = []
    for j in range(j, len(arr)):
        if j > 0 and arr[j - 1] == arr[j]:
            continue
        search_pair(arr, j, target, triplets)
    return triplets


def search_pair(arr, i, target, triplets):
    cur = arr[i]
    to_find = target - cur
    left = i + 1
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == to_find:
            triplets.append([cur, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right += 1
        elif arr[left] + arr[right] < to_find:
            left += 1
        else:
            right -= 1
    return triplets


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

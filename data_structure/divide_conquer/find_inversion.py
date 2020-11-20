#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: find_inversion.py
@time: 2020/9/25 10:23
@function:
find inversion pairs in a given list
e.g, list= [2,4,3,1,5,6]
inversion pairs are (2,1),(4,3),(4,1),(3,1)

the idea is using divide and conquer,  split the list into sub list1 and list2.
calculate the inversion number of sub1 and sub2, then in merge process, inversion =inv(s1)+inv(s2)+inv(s1,s2)

"""

global num
num = 0


def count(a, n):
    merge_count_sort(a, 0, n - 1)
    return num


def merge_count_sort(a, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_count_sort(a, start, mid)
    merge_count_sort(a, mid + 1, end)
    merge(a, start, mid, end)


def merge(a, left, mid, right):
    """
    double pointer i j, to run through list.
    with a tmp list to store smaller element, if a[i]>a[j],
    then mid-i+1 numbers in [i,mid] area is bigger than a[j], which is ensured by a is sorted.
    after sorted tmp list is inserted, re insert the tmp list to a, to achieve sort purpose.
    i,mid,j, right
    :param a:
    :param left:
    :param mid:
    :param right:
    :return:
    """
    i = left
    j = mid + 1
    k = 0
    tmp = []
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
            k += 1
        else:
            global num
            num += mid - i + 1
            tmp.append(a[j])
            k += 1
            j += 1
    while i <= mid:
        tmp.append(a[i])
        i += 1
    while j <= right:
        tmp.append(a[j])
        j += 1

    for i in range(right - left + 1):
        a[left + i] = tmp[i]


if __name__ == '__main__':
    arr = [2, 4, 3, 1, 5, 6]
    pairs = count(arr, 6)
    print(pairs)

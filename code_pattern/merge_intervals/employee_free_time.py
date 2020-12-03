#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: employee_free_time.py
@time: 2020/12/3 14:51
@function:
Employee Free Time (hard) #
For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
Our goal is to find out if there is a free interval that is common to all employees.
You can assume that each list of employee working hours is sorted on the start time.
Example 1:

Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: Both the employees are free between [3,5].
Example 2:

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employees are free between [4,6] and [8,9].
Example 3:

Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employees are free between [5,7].
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def find_employee_free_time(schedules):
    """
    sort the schedules, and find gap by no overlaps.
    :param schedules:
    :return:
    """
    result = []
    total_list = []
    # try to optimise the sort.
    cur_index = 0
    appended = True
    while appended:
        appended = False
        for i in range(len(schedules)):
            cur_len = len(schedules[i])
            # visit_index = cur_index
            if cur_index < cur_len:
                total_list.append(schedules[i][cur_index])
                appended = True
        cur_index += 1
    total_list.sort(key=lambda x: x.start)
    start, end = total_list[0].start, total_list[0].end
    n = len(total_list)
    for i in range(1, n):
        # if interval a b overlaps
        if total_list[i].start <= end:
            start = min(start, total_list[i].start)
            end = max(end, total_list[i].end)
        else:  # no overlaps,append gap and update a=b
            result.append([end, total_list[i].start])
            start, end = total_list[i].start, total_list[i].end

    return result


def test():
    input_schedules = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    assert [[3, 5]] == find_employee_free_time(input_schedules)


def test_1():
    input_schedules = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    assert [[4, 6], [8, 9]] == find_employee_free_time(input_schedules)


def test_2():
    input_schedules = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    assert [[5, 7]] == find_employee_free_time(input_schedules)


def test_3():
    input_schedules = [[Interval(1, 3)], [
        Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5)], [Interval(9, 12)]]
    assert [[5, 6], [7, 9]] == find_employee_free_time(input_schedules)


if __name__ == '__main__':
    test()

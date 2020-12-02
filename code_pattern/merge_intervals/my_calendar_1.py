#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: my_calendar_1.py
@time: 2020/12/2 15:58
@function:
leetcode 729


"""


class MyCalendar:

    def __init__(self):
        self.app = []

    def book(self, start: int, end: int) -> bool:
        new_interval = [start, end]
        if self.check_no_conflict(self.app, new_interval):
            self.app.append(new_interval)
            return True
        else:
            return False

    def check_no_conflict(self, ints, new_interval):

        intervals = ints.copy()
        intervals.append(new_interval)
        n = len(intervals)
        if n < 1:
            return True

        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            # here same a_end and b_start means not conflict
            if intervals[i][0] < end:

                return False
            else:
                start, end = intervals[i][0], intervals[i][1]
        return True

    # Your MyCalendar object will be instantiated and called as such:


# obj = MyCalendar()
# param_1 = obj.book(start,end)

def test():
    obj = MyCalendar()
    book_list = [[], [10, 20], [15, 25], [20, 30]]
    result = []
    for item in book_list:
        if len(item) > 1:
            start, end = item[0], item[1]
            result.append(obj.book(start, end))
    print(result)

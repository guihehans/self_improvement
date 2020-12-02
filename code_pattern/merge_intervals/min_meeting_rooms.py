#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: min_meeting_rooms.py
@time: 2020/12/2 16:45
@function:

"""

from heapq import *
from typing import List


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(meetings: List[Meeting]) -> int:
    n = len(meetings)
    if n < 2:
        return n
    meetings.sort(key=lambda meeting: meeting.start)
    rooms = [meetings[0]]

    for i in range(1, n):
        next_meeting = meetings[i]
        for j in range(len(rooms)):
            first_meeting = rooms[j]
            # all meetings iterated and find overlap
            if first_meeting.start <= next_meeting.start < first_meeting.end and j == len(rooms)-1:
                rooms.append(next_meeting)
                continue
            else:
                first_meeting.start = min(first_meeting.start, next_meeting.start)
                first_meeting.end = max(first_meeting.end, next_meeting.end)
                break

    return len(rooms)


def test():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


if __name__ == '__main__':
    test()

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

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


def min_meeting_rooms_my(meetings: List[Meeting]) -> int:
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
            if first_meeting.start <= next_meeting.start < first_meeting.end and j == len(rooms) - 1:
                rooms.append(next_meeting)
                continue
            else:
                first_meeting.start = min(first_meeting.start, next_meeting.start)
                first_meeting.end = max(first_meeting.end, next_meeting.end)
                break

    return len(rooms)


def min_meeting_rooms(meetings: List[Meeting]) -> int:
    n = len(meetings)
    if n < 2:
        return n
    meetings.sort(key=lambda x: x.start)
    min_heap = []
    min_room = 0
    for meeting in meetings:
        # if min_heap not empty and current meeting start after current smallest min_heap meeting's end
        # which means current meeting can be arranged after the min_heap[0]
        # pop the min_heap[0]
        if len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)
        # else, the meeting overlap with one meeting in heap, heappush it as open another room.
        heappush(min_heap, meeting)
        min_room = max(min_room, len(min_heap))

    return min_room


def test():
    min_room = min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])
    assert min_room == 2


def test_2():
    min_room = min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])
    assert min_room == 2


def test_3():
    min_room = min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])
    assert min_room == 1


def test_4():
    min_room = min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])
    assert min_room == 2


if __name__ == '__main__':
    test()

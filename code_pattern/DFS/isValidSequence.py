#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: isValidSequence.py
@time: 2020/12/11 16:17
@function:

"""

import json
from typing import List


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, sequence: List[int]) -> bool:
        if root is None or len(sequence) == 0 or sequence[0] != root.val:
            return False
        if root.left is None and root.right is None and len(sequence) == 1:
            return root.val == sequence[0]
        else:
            return self.isValidSequence(root.left, sequence[1:]) or self.isValidSequence(root.right, sequence[1:])


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            line = next(lines)
            arr = stringToIntegerList(line);

            ret = Solution().isValidSequence(root, arr)

            out = (ret);
            print(out)
        except StopIteration:
            break


def read_from_file():
    # Using readlines()
    file1 = open('my_file.txt', 'r')
    # lines = file1.readlines()

    count = 0
    # Strips the newline character
    line = next(file1)
    root = stringToTreeNode(line);
    line = next(file1)
    arr = stringToIntegerList(line);

    ret = Solution().isValidSequence(root, arr)

    out = (ret);
    print(out)


if __name__ == '__main__':
    read_from_file()

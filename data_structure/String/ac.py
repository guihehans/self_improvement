#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: ac.py
@time: 2020/9/23 14:51
@function:

an Aho-Corasick algorithm is a multiple string searching algorithm, which can search multiple pattern at same time.
"""


class AcTrie:
    class AcNode:
        def __init__(self, char):
            self.R = 256
            self.data = char
            self.children = [None] * self.R
            self.fail = None
            self.is_ending = False
            self.length = -1

    def __init__(self):
        self._root = self.AcNode('/')

    def insert(self, key):
        """
        insert a key str into acTrie
        :param key:
        :return:
        """
        p = self._root
        M = len(key)
        for i in range(M):
            index = ord(key[i])
            if p.children[index] is None:
                node = self.AcNode(key[i])
                p.children[index] = node
            p = p.children[index]
        p.is_ending = True
        p.length = M

    def contains(self, key) -> bool:
        """
        search if a key is in acTrie, true or false.
        :param key:
        :return:
        """
        p = self._root
        M = len(key)
        for i in range(M):
            index = ord(key[i])
            if p.children[index] is None:
                return False
            p = p.children[index]
        if not p.is_ending:
            return False
        else:
            return True


if __name__ == '__main__':
    pattern = 'ab'
    acTrie = AcTrie()
    acTrie.insert(pattern)
    assert acTrie.contains(pattern)
    assert not acTrie.contains('aa')

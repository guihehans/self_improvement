#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: ac.py
@time: 2020/9/23 14:51
@function:

an Aho-Corasick algorithm is a multiple string searching algorithm, which can search multiple pattern at same time.
"""
from itu.algs4.fundamentals.queue import Queue


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

    def build_fail(self):
        """

        build the fail pointer for each node.
        fail pointer is the longest suffix which can match the other's prefix,最长可匹配后缀
        and the pointer points to the prefix's last node.
        the building idea is like reversion.

        1.pc(p's child)'s fail is qc:  pc=qc when pc.data==qc.data. q =p.fail
        2.root's fail is none
        BFS the AcTrie and build fail for each node get from queue.

        :return:
        """
        queue = Queue()
        self._root.fail = None
        queue.enqueue(self._root)

        while not queue.is_empty():
            p = queue.dequeue()
            # BFS traverse the trie,each time set the p'c child pc's fail when p's fail is known.
            for pc in p.children:
                if pc is None:
                    continue
                if pc == self._root:
                    pc.fail = self._root
                else:
                    q = p.fail
                    while q:
                        # qc is the q'child which has same char with pc.
                        qc = q.children[ord(pc.data)]
                        if qc:
                            pc.fail = qc
                            break
                        # if qc not exist, q=q.fail, repeat.
                        q = q.fail
                    if q is None:
                        pc.fail = self._root
                queue.enqueue(pc)

    def search(self, txt: str):
        """
        the idea is check the fail pointer chain if the fail pointer is an ending.
        given txt str for search, the pattern list is inserted already.
        from p=root, check if p.children[index[i]] ==txt[i].
        if p has txt[i] children:
            p=p.children[index[i]]
            check whole fail pointer chain if has ending.
                if isending,  pos=i-tmp.length+1
            tmp=tmp.fail
        else: p.children[index[i]] is None and p!=root
                p=p.fail loop
        :param txt:
        :return:
        """
        n = len(txt)
        p = self._root
        for i in range(n):
            index = ord(txt[i])
            while p.children[index] is None and p != self._root:
                p = p.fail
            p = p.children[index]
            if p is None:
                p = self._root
            tmp = p
            while tmp != self._root:
                if tmp.is_ending:
                    pos = i - tmp.length + 1
                    print("匹配起始下标:{};长度:{}".format(pos, tmp.length))
                tmp = tmp.fail


if __name__ == '__main__':
    pattern = 'c'
    acTrie = AcTrie()
    acTrie.insert(pattern)
    assert acTrie.contains(pattern)
    assert not acTrie.contains('aa')
    pattern_list = ['bc', 'bcd', 'abce', 'ce']
    for p in pattern_list:
        acTrie.insert(p)

    acTrie.build_fail()
    acTrie.search("abcabce")

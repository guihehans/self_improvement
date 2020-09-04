#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: breadth_first_search.py
@time: 2020/9/4 14:16
@function:

"""
import math
from typing import Iterable

from itu.algs4.fundamentals.stack import Stack

from data_structure.Graph.Graph import Graph
from itu.algs4.fundamentals.queue import Queue


class BreadthFirstPath:
    def __init__(self, G: Graph, s: int):
        # the boolean array represent if vertex has path to source vertex s
        self._marked = [False] * G.V()
        # the int array to store one vertex's parent link.
        self._edgeTo = [0] * G.V()
        # the record dist array to given source s
        self._dist_to = [math.inf] * G.V()
        self._validateVertex(s)
        self._bfs(G, s)

    def _validateVertex(self, v):
        """
        raise error if v<0 or v>V
        :param v:
        :return:
        """
        V = len(self._marked)
        if v < 0 or v > V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V - 1))

    def _bfs(self, G: Graph, s: int):
        """
        bfs to search for shortest path from source s to all vertex

        :param G:
        :param s:
        :return:
        """
        queue = Queue()
        self._dist_to[s] = 0
        self._edgeTo[s] = 0
        self._marked[s] = True
        queue.enqueue(s)

        while not queue.is_empty():
            v = queue.dequeue()
            for w in G.adj(v):
                if not self._marked[w]:
                    self._marked[w] = True
                    self._edgeTo[w] = v
                    self._dist_to[w] = self._dist_to[v] + 1
                    queue.enqueue(w)

    def has_path_to(self, v) -> bool:
        """
        find paths in G from source s to v
        :param v:
        :return:
        """
        return self._marked[v]

    def dist_to(self, v: int):
        """
        return the shortest dist from s to v

        :param v:
        :return:
        """
        if self.has_path_to(v):
            return self._dist_to[v]

    def path_to(self, v: int) -> Iterable:
        """
        return an iterable path object which is shortest from s to v

        :param v:
        :return:
        """
        if not self.has_path_to(v):
            return None
        path = Stack()
        x = v
        while self._dist_to[x] != 0:
            path.push(x)
            x = self._edgeTo[x]
        path.push(x)
        return path


if __name__ == "__main__":
    import sys
    from itu.algs4.stdlib import stdio
    from itu.algs4.graphs.graph import Graph
    from itu.algs4.stdlib.instream import InStream

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    s = int(sys.argv[2])
    bfs = BreadthFirstPath(G, s)

    for v in range(G.V()):
        if bfs.has_path_to(v):
            stdio.writef("%d to %d (%d):  ", s, v, bfs.dist_to(v))
            for x in bfs.path_to(v):
                if x == s:
                    stdio.write(x)
                else:
                    stdio.writef("-%i", x)
            stdio.writeln()
        else:
            stdio.writef("%d to %d (-):  not connected\n", s, v)

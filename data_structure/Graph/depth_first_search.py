#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: depth_first_search.py
@time: 2020/9/3 14:10
@function:

"""
from data_structure.Graph.graph import Graph


class DepthFirstSearch:
    def __init__(self, G: Graph, s):
        """
        given the graph G, and vertex s, find all connected vertexes to s.
        :param G:
        :param s:
        """
        self._marked = [False] * G.V()
        self._count = 0
        self._validate_vertex(s)
        self._dfs(G, s)

    def _validate_vertex(self, v):
        """
        validate a vertex index.

        :param v:
        :return:
        """
        # throw an ValueError unless 0 <= v < V
        V = len(self._marked)
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V - 1))

    def _dfs(self, G, s):
        """
        DepthFirstSearch.
        1. marked the current node as visited,count++
        2. in current node's adj list which is not visited,recursively do DFS(G,curent adjnode)


        :param G:
        :param s:
        :return:
        """
        self._marked[s] = True
        self._count += 1
        for w in G.adj(s):
            if not self._marked[w]:
                self._dfs(G, w)

    def marked(self, v) -> bool:
        """
        return is v connected to s

        :param v:
        :return:
        """
        return self._marked[v]

    def count(self) -> int:
        """
        return how many vertices connected to s

        :return:
        """
        return self._count


if __name__ == '__main__':
    from itu.algs4.graphs.graph import Graph
    from itu.algs4.stdlib.instream import InStream
    from itu.algs4.stdlib import stdio
    import sys

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    s = int(sys.argv[2])
    search = DepthFirstSearch(G, s)
    for v in range(G.V()):
        if search.marked(v):
            stdio.writef("%i ", v)
    stdio.writeln()

    if search.count() != G.V():
        stdio.writeln("G is NOT a connected graph")
    else:
        stdio.writeln("G is a connected graph")

#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: depth_first_path.py
@time: 2020/9/3 15:53
@function:

"""

from itu.algs4.fundamentals.stack import Stack

from data_structure.Graph.graph import Graph


class DepthFirstPath:
    def __init__(self, G: Graph, s):
        self._marked = [False] * G.V()  # now represent if index vertex has path to source
        # last vertex on known path to this vertex. it's a parent link tree which store the parent
        self._edgeTo = [0] * G.V()
        self._s = s  # source
        self._validateVertex(s)
        self._dfs(G, s)

    def _dfs(self, G, v):
        self._marked[v] = True
        for w in G.adj(v):
            if not self._marked[w]:
                # record first time find edge(w,v) w's parent set to v.
                self._edgeTo[w] = v
                self._dfs(G, w)

    def _validateVertex(self, v):
        V = len(self._marked)
        if v < 0 or v > V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V - 1))

    def has_path_to(self, v):
        self._validateVertex(v)
        return self._marked[v]

    def path_to(self, v):
        """
        Returns a path between the source vertex s and vertex v, or
        None if no such path.
        :param v: the vertex
        :returns: the sequence of vertices on a path between the source vertex
                   s and vertex v, as an Iterable
        :raises ValueError: unless 0 <= v < V
        """
        self._validateVertex(v)
        if not self._marked[v]: return None
        path = Stack()
        w = v
        while w != self._s:
            path.push(w)
            # find w's parent link vertex,recursively until reach source.
            w = self._edgeTo[w]
        path.push(self._s)
        return path


if __name__ == "__main__":
    from itu.algs4.stdlib import stdio
    from itu.algs4.graphs.graph import Graph
    from itu.algs4.stdlib.instream import InStream
    import sys

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    s = int(sys.argv[2])
    dfs = DepthFirstPath(G, s)

    for v in range(G.V()):
        if dfs.has_path_to(v):
            stdio.writef("%d to %d:  ", s, v)
            for x in dfs.path_to(v):
                if x == s:
                    stdio.write(x)
                else:
                    stdio.writef("-%i", x)
            stdio.writeln()
        else:
            stdio.writef("%d to %d:  not connected\n", s, v)

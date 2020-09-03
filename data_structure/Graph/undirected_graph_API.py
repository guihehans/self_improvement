#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: undirected_graph_API.py
@time: 2020/9/1 15:26
@function:

"""
from data_structure.foundamental.Bag import Bag


class Graph:
    def __init__(self, V):
        if V < 0:
            raise ValueError("Number of vertices mus be non-negative")
        self._V = V
        self._E = 0
        self._adj = []
        # init the adj list, size is the V size. the index of list represent the vertex
        for _ in range(V):
            self._adj.append(Bag())

    @staticmethod
    def from_stream(stream):
        V = stream.readInt()
        if V < 0:
            raise ValueError("Number of vertices must be nonnegative")
        g = Graph(V)  # construct this graph
        E = stream.readInt()  # read E
        if E < 0:
            raise ValueError("Number of edges in a Graph must be nonnegative")

        for _ in range(E):
            # add an edge
            v = stream.readInt()
            w = stream.readInt()
            g.add_edge(v, w)
        return g

    def add_edge(self, v, w):
        # validate v w
        self._validateVertex(v)
        self._validateVertex(w)
        self._adj[v].add(w)
        self._adj[w].add(v)
        self._E += 1

    def V(self):
        """
        Returns the number of vertices in this graph.

        :returns: the number of vertices in this graph.
        """
        return self._V

    def E(self):
        """
        Returns the number of edges in this graph.

        :returns: the number of edges in this graph.
        """
        return self._E

    def _validateVertex(self, v):
        # throw a ValueError unless 0 <= v < V
        if v < 0 or v >= self._V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, self._V))

    def adj(self, v):
        """
        return the adjacent node set of given node.
        the data type is a Bag can be iterate.

        :return:
        """
        self._validateVertex(v)
        return self._adj[v]

    def degree(self, v):
        """
        return the degree of vertex v
        since the graph is undirected, the degree is the LinkedNode List size.

        :param v:
        :return:
        """
        self._validateVertex(v)
        return self._adj[v].size()

    def __repr__(self):
        """
        Returns a string representation of this graph.

        :returns: the number of vertices V, followed by the number of edges E,
                    followed by the V adjacency lists
        """
        s = ["{} vertices, {} edges\n".format(self._V, self._E)]
        for v in range(self._V):
            s.append("%d : " % (v))
            for w in self._adj[v]:
                s.append("%d " % (w))
            s.append("\n")

        return "".join(s)


if __name__ == "__main__":
    import sys

    from itu.algs4.stdlib import stdio
    from itu.algs4.stdlib.instream import InStream

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    stdio.writeln(G)

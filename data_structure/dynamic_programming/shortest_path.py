"""
@author: guihehans
@file: shortest_path.py 
@time: 2020/11/22 10:03
@function:

There's a n*n matrix w[n][n] which store the values of each node's distance. start from (0,0), end at (n-1,n-1).
can only go downward or go right.
the path is the sum of passing node distance.
find the shortest path from (0,0) to (n-1,n-1)

"""
import math


class ShortestPath:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.shortest_path = math.inf
        # init states
        self.states = [[-1 for i in range(self.n)] for j in range(self.n)]
        # init mem for dp_mem
        self.mem = [[0 for i in range(self.n)] for j in range(self.n)]

    def backtracking(self, i, j, cur_shortest_path):
        cur_shortest_path += self.matrix[i][j]
        # termination condition
        if i == self.n - 1 and j == self.n - 1:
            if cur_shortest_path < self.shortest_path:
                self.shortest_path = cur_shortest_path
            return

        if i < self.n - 1:
            self.backtracking(i + 1, j, cur_shortest_path)
        if j < self.n - 1:
            self.backtracking(i, j + 1, cur_shortest_path)

    def dp_states(self):
        states = self.states
        matrix = self.matrix
        n = self.n

        for i in range(0, n):
            for j in range(0, n):
                if i == 0 and j == 0:
                    states[i][j] = matrix[i][j]
                elif i == 0:
                    states[i][j] = states[i][j - 1] + matrix[i][j]
                elif j == 0:
                    states[i][j] = states[i - 1][j] + matrix[i][j]
                elif i - 1 >= 0 and j - 1 >= 0:
                    states[i][j] = min(states[i - 1][j], states[i][j - 1]) + matrix[i][j]

        self.shortest_path = states[n - 1][n - 1]
        return self.shortest_path

    def min_dist(self, i, j):
        """
        use a mem[][] to store calculated path.
        min_dist[i][j]= min(min_dist_left,min_dist_top)+m[i][j]
        with the function.
        init invoke dp_mem(n-1,n-1)
        :param i:
        :param j:
        :return:
        """

        if i == 0 and j == 0:
            self.mem[0][0] = self.matrix[i][j]
            return self.mem[0][0]
        if self.mem[i][j] > 0:
            return self.mem[i][j]
        min_left = math.inf
        if j - 1 >= 0:
            min_left = self.min_dist(i, j - 1)
        min_top = math.inf
        if i - 1 >= 0:
            min_top = self.min_dist(i - 1, j)

        cur_min_dist = self.matrix[i][j] + min(min_left, min_top)
        self.mem[i][j] = cur_min_dist
        return cur_min_dist


def f():
    matrix = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    shortest_path = ShortestPath(matrix)
    shortest_path.backtracking(0, 0, 0)
    print(shortest_path.shortest_path)


def f_1():
    matrix = [[1, 3], [2, 1]]
    shortest_path = ShortestPath(matrix)
    shortest_path.backtracking(0, 0, 0)
    print(shortest_path.shortest_path)


def f_dp_states_array():
    matrix = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    shortest_path = ShortestPath(matrix)
    shortest_path.dp_states()
    print(shortest_path.shortest_path)


def f_dp_mem():
    matrix = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    shortest_path = ShortestPath(matrix)
    min_dist=shortest_path.min_dist(3, 3)
    print(min_dist)


if __name__ == '__main__':
    f()
    f_1()
    f_dp_states_array()
    f_dp_mem()

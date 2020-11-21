"""
@author: guihehans
@file: triangle_find_shortest_path.py 
@time: 2020/11/21 19:52
@function:

思考题  改造杨辉三角，数字可任意。 但任意节点只能通往相邻下层节点。
定义顶层到底层经过的所有数字之和为路径长度，求顶层到底层最短路径.
"""
import math


def triangle_find_shortest_path(matrix, col, depth):
    """
    the triangle can use 2d matrix to represent the triangle.
    depth is
    :param matrix: the triangle data
    :param col: matrix col numbers.
    :param depth: node total numbers
    :return:
    """
    # init states array. col is each node. value is current acc path.
    states = [[math.inf for j in range(col)] for i in range(depth)]
    states[0][0] = matrix[0][0]
    for i in range(0, depth - 1):
        for j in range(len(matrix[i])):
            left_x, left_y = i + 1, j
            r_x, r_y = i + 1, j + 1
            #  states[i + 1][left_y]=min{states[i][j] + matrix[left_x][left_y]}
            #  same as states[i + 1][right_y]
            if states[left_x][left_y] > states[i][j] + matrix[left_x][left_y]:
                states[i + 1][left_y] = states[i][j] + matrix[left_x][left_y]
            if states[r_x][r_y] > states[i][j] + matrix[r_x][r_y]:
                states[i + 1][r_y] = states[i][j] + matrix[r_x][r_y]

    shortest_path = min(states[depth - 1])
    # print path
    cur_path = shortest_path
    found_j = 0
    for i in range(depth - 1, 0, -1):
        for j in range(len(matrix[i])):
            # use or short path to go to found_j. since sometimes there exists same states in upper stage.
            # use found_j to find right states. and treat 1 time special.
            if states[i][found_j] == cur_path or states[i][j] == cur_path:
                if i == depth - 1:
                    print("level:{},node index:{},value:{} in shortest path".format(i, j, matrix[i][j]))
                    found_j = j
                cur_path -= matrix[i][found_j]
                last_i = i - 1
                last_j_l = found_j - 1
                last_j_r = found_j
                if last_j_l in range(len(matrix[last_i])):
                    if states[last_i][last_j_l] == cur_path:
                        print("level:{},node index:{},value:{} in shortest path".format(last_i, last_j_l,
                                                                                        matrix[last_i][last_j_l]))
                        found_j = last_j_l
                        break
                if last_j_r in range(len(matrix[last_i])):
                    if states[last_i][last_j_r] == cur_path:
                        print("level:{},node index:{},value:{} in shortest path".format(last_i, last_j_r,
                                                                                        matrix[last_i][last_j_r]))
                        found_j = last_j_r
                        break

    return shortest_path


def f():
    matrix = [[5], [7, 8], [2, 3, 4], [4, 9, 6, 1], [2, 7, 9, 4, 5]]
    col = len(matrix[len(matrix) - 1])
    depth = len(matrix)
    shortest_path = triangle_find_shortest_path(matrix, col, depth)
    print(shortest_path)


def f_1():
    matrix = [[5], [7, 8], [4, 3, 2], [4, 9, 6, 1], [2, 7, 9, 4, 5]]
    col = len(matrix[len(matrix) - 1])
    depth = len(matrix)
    shortest_path = triangle_find_shortest_path(matrix, col, depth)
    print(shortest_path)


if __name__ == '__main__':
    f()
    print(">.............")
    f_1()

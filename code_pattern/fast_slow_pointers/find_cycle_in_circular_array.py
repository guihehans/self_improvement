"""
@author: guihehans
@file: find_cycle_in_circular_array.py 
@time: 2020/11/28 22:18
@function:

"""


def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] > 0
        slow, fast = i, i
        while True:
            slow = find_next_index(arr, slow, is_forward)
            fast = find_next_index(arr, fast, is_forward)
            if fast != -1:
                fast = find_next_index(arr, fast, is_forward)
            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True
    # after traverse all element,if not return,return false
    return False


def find_next_index(arr, idx, is_forward):
    # return -1 for error

    # check if direction change
    direction = arr[idx] > 0
    if is_forward is not direction:
        return -1

    cur = arr[idx]
    next_index = (idx + cur) % len(arr)
    if next_index == idx:
        next_index = -1

    return next_index


def test():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


if __name__ == '__main__':
    test()
    print(-1 % 5)

def max_sub_array_of_size_k(k, arr):
    window_start, window_end, window_sum = 0, 0, 0.0
    max_index = 0
    tmp_max = 0
    result_list = []
    for i, value in enumerate(arr):
        window_sum += value
        if i >= k - 1:
            if tmp_max == 0 or tmp_max < window_sum:
                tmp_max = window_sum
                max_index = window_start
            window_sum -= arr[window_start]
            window_start += 1

    return tmp_max,arr[max_index:max_index+k]


def main():
    result = max_sub_array_of_size_k(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("maximum sum is " + str(result))


main()
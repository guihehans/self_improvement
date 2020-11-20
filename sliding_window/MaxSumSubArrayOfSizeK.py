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

    return tmp_max, arr[max_index:max_index + k]


def max_sub_array_of_size_k_ref(k, arr):
    window_start, window_end, window_sum = 0, 0, 0
    max_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:  # when end >= k-1
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


def main():
    f = max_sub_array_of_size_k_ref
    result = f(3, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("maximum sum is " + str(result))


if __name__ == '__main__':
    main()

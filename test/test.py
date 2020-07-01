def find_averages_of_subarrays(k: int, arr: list):
    """
    the function is to find the averages of k size sub_arrays in given array.
    the slide method is, treat each subarray to cal avg as a window.
    when window slides each time, - head and + tail.
    append each avg to result list.
    use window_start and window_end as head tail pointer.

    :param k: the size of subarray
    :param arr : the given array
    :return:list. the list of averages of k size sub_arrays
    """
    window_start = 0
    window_end = 0
    window_sum = 0.0
    result_list = []
    for i, value in enumerate(arr):
        window_sum += value
        # do the - head,+ tail procedure when index reach window_end
        if i >= k-1:
            result_list.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1
    return result_list



def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()

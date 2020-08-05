class Solution:
    def merge(self, n, p, q, r):
        """
        for given two sorted array n[p:q],n[q+1:r]
        ,merge and sort the arrays.
        :param n:the whole array to manipulate
        :param p:upper index n[p:q]
        :param q:middle index n[p:q]
        :param r: end index n[q+1:r]
        :return: the sorted array n
        """
        max = 65536
        n1 = q - p + 1
        n2 = r - (q + 1) + 1
        # print(n1)
        # print(n2)
        arr1 = n[p:q + 1].copy()
        arr2 = n[q + 1:r + 1].copy()
        # insert a max value to copied sub array to
        # ensure the last element in empty array will be larger
        # so the other arrays element will move back to original n

        arr1.append(65536)
        arr2.append(65536)
        # print(arr1)
        # print(arr2)
        i = 0
        j = 0
        for k in range(p, r + 1):
            # print(k)
            if arr1[i] < arr2[j]:
                n[k] = arr1[i]
                i = i + 1
            else:
                n[k] = arr2[j]
                j = j + 1

        return n[p:r + 1]

    def merge_sort(self, n, p, r):
        """

        :param n:
        :param p:
        :param r:
        :return:
        """
        # 1. divide the whole list into each 2-element array
        print('merge from {} to {}'.format(p, r))
        if p < r:
            # 下取整找到中间边界
            q = (p + r) // 2
            print('next merge from {} to {}'.format(p, q))
            # divide and recursive invoke
            self.merge_sort(n, p, q)
            self.merge_sort(n, q + 1, r)
            print(self.merge(n, p, q, r))
            return n


if __name__ == "__main__":
    # nums = [2, 11, 7, 15]
    # target = [2, 7, 11, 15]
    # assert (Solution().merge_sort(nums) == nums)
    # nums = [3, 2, 4]
    # target = [2, 3, 4]
    # assert (Solution().merge_sort(nums) == target)
    nums=[3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
    # print(Solution().merge_sort(nums))
    # nums = [3, 44, 38, 5, 47, 15, 36, 26]
    # nums = [2, 11, 7, 15]
    print(Solution().merge_sort(nums,0,len(nums)-1))
    # print(Solution().merge(nums, 2, 2, 3))

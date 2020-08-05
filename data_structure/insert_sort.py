class Solution:
    def insert_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sorted,unsorted list
        for j in range(1, len(nums)):
            key = nums[j]
            # insert nums[j] to sorted listA[1,j-1]
            i = j - 1
            while i >= 0 and nums[i] > key:
                # move the nums backward
                nums[i + 1] = nums[i]
                i = i - 1
            # insert key
            nums[i + 1] = key
        return nums


if __name__ == "__main__":
    nums = [2, 11, 7, 15]
    target = [2, 7, 11, 15]
    assert (Solution().insert_sort(nums) == nums)
    nums = [3, 2, 4]
    target = [2, 3, 4]
    assert (Solution().insert_sort(nums) == target)
    nums=[3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
    print(Solution().insert_sort(nums))

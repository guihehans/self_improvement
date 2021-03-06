import unittest


def insert_sort(nums):
    """
    1. treat nums[0:i] as sorted,nums[i:len(arr)] unsorted. i range(1,len(nums))
    2. each step, the to insert card is nums[i], looply compare it the the element in sorted list. if
        nums[sorted_index] > card, move it backward. until reach an element < card.
    3. insert the card to where it should be(sorted_index+1)
    4. finished when i reach end.

    :type nums: List[int]
    :rtype: List[int]
    """
    # sorted,unsorted list
    for i in range(1, len(nums)):
        card = nums[i]
        last_sorted_index = i - 1
        while nums[last_sorted_index] > card and last_sorted_index >= 0:
            nums[last_sorted_index + 1] = nums[last_sorted_index]
            last_sorted_index -= 1
        # insert the card into sorted part
        nums[last_sorted_index + 1] = card
    return nums


class TestCase(unittest.TestCase):
    def test(self):
        arr = [2, 5, 1, 8]
        target = [1, 2, 5, 8]
        self.assertTrue(target == insert_sort(arr))

    def test_1(self):
        nums = [2, 11, 7, 15]
        target = [2, 7, 11, 15]
        self.assertTrue(insert_sort(nums) == target)

    def test_2(self):
        nums = [3, 2, 4]
        target = [2, 3, 4]
        self.assertTrue(insert_sort(nums) == target)

    def test_3(self):
        nums = [4, 3, 2]
        target = [2, 3, 4]
        self.assertTrue(insert_sort(nums) == target)


if __name__ == '__main__':
    unittest.main()

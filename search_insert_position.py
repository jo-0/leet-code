# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/


from typing import List


def search_insert(nums: List[int], target: int) -> int | None:
    try:
        return nums.index(target)
    except ValueError:
        for i in range(len(nums)):
            # if target is the last element
            if target > nums[len(nums) - 1]:
                return len(nums)

            if target < nums[i]:
                return i
            else:
                continue


print((search_insert(nums=[1, 3, 5, 6], target=5)))

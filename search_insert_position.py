"""
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1. 1 <= nums.length <= 104
2. -104 <= nums[i] <= 104
3. nums contains distinct values sorted in ascending order.
4. -104 <= target <= 104
"""

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

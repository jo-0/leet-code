# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/


def rotate(nums, k) -> None:
    """
    Rotate array k times
    """
    new_list = []
    new_list = nums[-k:]
    new_list += nums[:k + 1]
    print("new 2 = ", new_list)


rotate([1, 2, 3, 4, 5, 6, 7], 3)
rotate([-1, -100, 3, 99], 2)

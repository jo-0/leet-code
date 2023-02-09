# 801. Minimum Swaps To Make Sequences Increasing
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/


def minimum_swap(A, B):
    n1, s1 = 0, 1  # 0, 1
    for i in range(1, len(A)):
        n2 = s2 = float("inf")
        if A[i - 1] < A[i] and B[i - 1] < B[i]:
            n2 = min(n2, n1)
            s2 = min(s2, s1 + 1)
        if A[i - 1] < B[i] and B[i - 1] < A[i]:
            n2 = min(n2, s1)
            s2 = min(s2, n1 + 1)

        n1, s1 = n2, s2

    return min(n1, s1)


print(minimum_swap([3, 2], [1, 5]))

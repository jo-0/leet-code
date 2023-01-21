# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    num_str = str(x)
    length = len(num_str) - 1
    reverse = ''
    while (length >= 0):
        reverse += num_str[length]
        length -= 1

    return True if int(reverse) == x else False


print(is_palindrome(121))

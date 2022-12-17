"""
Make a palindrome

Palindromes are strings that read the same from the left or right (For example, madam). Similarly, any number that is
read the same from the left or the right is a plaindromic number (For example, 101101).

You are given a number N and a maximum number of digits K that you can change in this number. Modify the number, one
digit at a time, to create the largest possible palindromic number under the limit to the number of changes. The
leading digit (left-most digit) of the number cannot be made zero. As that would reduce the number of digits in the
number. For example, you can change 1110 to 1111, but should not change it to 0110.

Given a number, and a maximum number of changes allowed, create the largest possible palindromic number or print -1 if
it is not possible to create a palindromic number within the allowed number of changes.
-----------------------------------------------------------------------------------------------------------------------
Input:
The first line in the test case contains two space-separated integers, D and K the number of digits in the number and
the maximum number of changes allowed.
The second line in the test case contains an D -digit number N
-----------------------------------------------------------------------------------------------------------------------
Output:
The output should be an integer as mentioned above.
-----------------------------------------------------------------------------------------------------------------------
Explanation:

Given D = 5 K = 2
The 5-digit number N is 52234
First, we change the second digit from 2 to 3.
Next, we change the last digit from 4 to 5
So the output is 53235

Sample Input 1
5 2
52234

Sample Output 1
53235

Sample Input 2
5 3
12335

Sample Output 2
93339

Sample Input 3
7 4
2121352

Sample Output 3
9531359

Sample Input 4
20 5
12345678901234567890

Sample Output 4
- 1
"""

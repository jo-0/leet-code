"""
Detect Cycle in Directed Graph

Given N vertices numbered 1 to N of a directed graph along with edges, write a program to check if there exists any
cycle.
Note: A vertex with an edge to itself is also considered a cycle.

-----------------------------------------------------------------------------------------------------------------------
Input
In each test case, the first line contains a single integer N representing the number of vertices. N lines follow.
In each test case, the next N lines contain space-separated integers.
In each line, the first integer has an edge with all the following integers (if they exist) except the last one. -1 at
the end represents the end of the line.
-----------------------------------------------------------------------------------------------------------------------
Output
For each test case, print Yes if there exists any cycle, otherwise, print No in a newline.
-----------------------------------------------------------------------------------------------------------------------
Constraints
1 <= T <= 3
2 <= N <= 5000
-----------------------------------------------------------------------------------------------------------------------
Explanation

Sample Output 1
Given T= 1 N = 5

2<----1
|  /  |
4---->5
\    /
   3

The cycle present in 1-2-4-1. The output is `YES`

Sample Input 1
5
1 5 2 - 1
2 4 5 - 1
3 5 - 1
4531-1
5 - 1

Sample Output 1
Yes

Sample Input 2
5
12-1
2 4 - 1
3 4 - 1
4 - 1
5 4 - 1

Sample Output 2
No

Sample Input 3
2
1 2 - 1
2 1 - 1

Sample Output 3
Yes
"""

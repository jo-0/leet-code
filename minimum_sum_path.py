"""
Maximum Sum Path

Given a list of numbers representing nodes of a binary tree along with null which represents NULL in level-order
sequence, write a program to construct a binary tree using this list and find the maximum sum path.

The path should be unidirectional. That means once a path goes through a node, it cannot come back to the same node
again.

Note: The path can start from any node, and it need not pass through the root.
-----------------------------------------------------------------------------------------------------------------------
Input
The first line contains space-separated integers and strings.
Note: Other than integers, all the string values in the input will be nUll
-----------------------------------------------------------------------------------------------------------------------
Output
The output contains a single integer representing the sum of the maximum sum path.
-----------------------------------------------------------------------------------------------------------------------
Constraints
2 <= Number of nodes <= 1.5 * 10^5
-10^5 <= Numbers in list < = 10^5
-----------------------------------------------------------------------------------------------------------------------
Explanation
Given Level-Order = -2 3 0 - 1 8 7 6

                -2
                /\
               /  \
              /    \
             /      \
            3        0
            /\       /\
           /  \     /  \
         -1    8   7    6

Max Sum = 8 + 3 + -2 + 0 + 7 = 16

Given nodes don't form a full binary tree.
So the output is `False`

Sample Input 1
-2 3 0 -1 8 7 6

Sample Output 1
16

Sample Input 2
1 2 3 4 9 10 null 1

Sample Output 2
25
"""

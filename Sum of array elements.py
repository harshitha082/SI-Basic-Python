"""
Given an array of integers, find the sum of the elements of the given array.
Note: Try to solve this without declaring/storing the array elements.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array and second line contains the elements of the array.

Constraints

1 <= T <= 100
1 <= N <= 1000
1 <= ar[i] <= 1015

Output Format

For each test case, print the sum of the elements of the array, separated by new line.

Sample Input 0

2
3
5 15 3 
2
70 100 
Sample Output 0

23
170
Explanation 0

Self Explanatory
"""


T=int(input())
for i in range(T):
    N=int(input())
    x = [int(x) for x in input().split()]
    sum = 0
    for i in range(N):
        sum+=x[i]
    print(sum)
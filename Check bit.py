"""
Check bit

In a given integer N, check whether the ith bit is set or not.

Input Format

First and only line of input contains N and i.

Constraints

0 <= N <= 109
0 <= i <= 30

Output Format

Print "true" if ith bit is set in the given integer N, "false" otherwise.

Sample Input 0

10 1
Sample Output 0

true
Explanation 0

The binary form of 10 is: 1010. So the 1st bit in 10 is set. Note that LSB bit is referred as 0th bit.

"""

a=[int(x) for x in input().split()]
if (a[0]>>a[1])%2==1:
    print("true")
else:
    print("false")


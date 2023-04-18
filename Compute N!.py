"""
Compute N!

Given a non-negative number - N, print N!

Input Format

First and only line of input contains a number - N.

Constraints

0 <= N <= 10

Output Format

Print factorial of N.

Sample Input 0

5
Sample Output 0

120
Explanation 0

Self Explanatory

"""

N=int(input())
fac=1
for i in range(1,N+1):
    fac*=i
print(fac)
    
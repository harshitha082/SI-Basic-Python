"""
Digits sum

Given a non-negative integer - N, print the sum of digits of the given number.

Input Format

First and only line of input contains a non-negative integer N.

Constraints

0 <= length(N) <= 103

Output Format

Print the sum of digits of the given number.

Sample Input 0

164
Sample Output 0

11
Explanation 0

Self Explanatory

"""

N=int(input())
def Sum(N):
    Sum=0
    while N!=0:
        Sum+=(N%10)
        N=N//10
    return Sum
print(Sum(N))
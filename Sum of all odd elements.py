"""
Sum of all odd elements

Print sum of all odd elements in an array.

Input Format

First line of input contains N - the size of the array and second line contains array elements.

Constraints

1 <= N <= 100
-109 <= ar[i] <= 109

Output Format

Print sum of all odd elements of the given array.

Sample Input 0

5
6 9 8 4 3
Sample Output 0

12
Explanation 0

Self Explanatory

"""

a = input()
l = list(map(int,input().split()))
sum=0
for i in range(len(l)):
    if l[i]%2 !=0:
        sum += l[i]
print(sum)
        
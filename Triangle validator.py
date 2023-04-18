"""
Triangle validator

Given the length of 3 sides of a triangle, check whether the triangle is valid or not.

Input Format

First and only line of input contains three integers A, B, C - length of sides of the triangle.

Constraints

1 <= A, B, C <= 109

Output Format

Print "Yes" if you can construct a triangle with the given three sides, "No" otherwise.

Sample Input 0

4 3 5
Sample Output 0

Yes
Explanation 0

Self Explanatory

"""

A,B,C=[int(x) for x in input().split()]
if ((A+B)>C) and ((A+C)>B) and ((C+B)>A):
    print("Yes")
else:
    print("No")
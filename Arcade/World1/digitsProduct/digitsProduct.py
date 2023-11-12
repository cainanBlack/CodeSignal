"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
solution(product) = 26;
For product = 19, the output should be
solution(product) = -1.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer product

Guaranteed constraints:
0 ≤ product ≤ 600.

[output] integer


Solution: Cainan Black
"""

def solution(p):
    
    if p == 0: 
        return 10
        
    for i in range(3600):
        a = 1
        for j in str(i):
            a *= int(j)
        if a == p: return i
    return -1

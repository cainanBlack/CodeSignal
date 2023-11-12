"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
solution(n, firstNumber) = 7.



Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

A positive even integer.

Guaranteed constraints:
4 ≤ n ≤ 20.

[input] integer firstNumber

Guaranteed constraints:
0 ≤ firstNumber ≤ n - 1.

[output] integer


Solution: Cainan Black
"""

def solution(n, fnum):
    l1 = []
    l2 = []
    
    for i in range(n):
        if i < int(n/2):
            l1.append(i)
        else:
            l2.append(i)
            
    for b in range(len(l1)):
        if l1[b] == fnum:
            return l2[b]
            
    for m in range(len(l2)):
        if l2[m] == fnum:
            return l1[m]

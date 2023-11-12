"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
10 ≤ n ≤ 106.

[output] integer


Solution: Cainan Black
"""

def solution(n):
    x=list(str(n))
    test=[]
    for i in range(len(x)):
        x.pop(i)
        test.append(''.join(x))
        x=list(str(n))
        
    return int(max(test))

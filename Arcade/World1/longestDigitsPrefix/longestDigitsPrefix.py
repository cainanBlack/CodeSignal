"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string inputString

Guaranteed constraints:
3 ≤ inputString.length ≤ 100.

[output] string


Solution: Cainan Black
"""

def solution(r):
    res = ""
    for i in r:
        if i.isdigit():
            res += i
        else:
            break
    return res

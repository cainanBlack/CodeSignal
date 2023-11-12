"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                     "*abc*",
                     "*ded*",
                     "*****"]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string picture

A non-empty array of non-empty equal-length strings.

Guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.

[output] array.string

The same matrix of characters, framed with a border of asterisks of width 1.


Solution: Cainan Black
"""

def solution(picture):
    edgeLen = len(picture[0]) + 2
    bor = "*"
    newL = [bor * edgeLen]
    for i in range(len(picture)):
        picture[i] = str(bor+picture[i]+bor)
        newL.append(picture[i])
    newL.append(bor*edgeLen)
    #print(newL)
    return newL


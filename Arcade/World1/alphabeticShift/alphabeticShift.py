"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.


Solution: Cainan Black
"""

def solution(word):
    alph = "abcdefghijklmnopqrstuvwxyz"
    new = ""
    for i in word:
        for b in range(len(alph)):
            if i == 'z':
                new += 'a'
                break
            if i == alph[b]:
                new += alph[b+1]
                break
    return new

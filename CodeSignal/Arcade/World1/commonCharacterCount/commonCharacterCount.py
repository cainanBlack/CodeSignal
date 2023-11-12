"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer


Solution: Cainan Black
"""

def solution(s1, s2):
    l1 = []
    l2 = []
    shared = 0
    for i in s1:
        l1.append(i)
    for b in s2:
        l2.append(b)
    l1.sort()
    l2.sort()
    
    for k in range(len(l1)):
        for m in range(len(l2)):
            if l1[k] == l2[m]:
                del l2[m]
                shared += 1
                break
        
    return shared

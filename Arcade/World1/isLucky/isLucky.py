"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.


Solution: Cainan Black
"""

def solution(n):
    nL = []
    l1 = []
    l2 = []
    
    for i in str(n):
        nL.append(i)
        
    for b in range(len(nL)):
        if int(b) >= int(len(nL)/2):
            l2.append(int(nL[b]))
        else:
            l1.append(int(nL[b]))

    if sum(l1) == sum(l2):
        print("True")
        return True
    else:
        print("False")
        return False

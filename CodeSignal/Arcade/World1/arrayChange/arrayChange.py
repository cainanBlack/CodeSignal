"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-105 ≤ inputArray[i] ≤ 105.

[output] integer

The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.


Solution: Cainan Black
"""

def solution(A):
    inc = 0
    temp = 0
    for i in range(len(A)-1):
            if A[i] > A[i+1]:
                temp = A[i] - A[i+1] + 1
                inc += temp
                A[i+1] += temp
            if A[i] == A[i+1]:
                A[i+1] = A[i+1] + 1
                inc += 1
    return inc        

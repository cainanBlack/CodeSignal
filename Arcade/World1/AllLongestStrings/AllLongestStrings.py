"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.


Solution: Cainan Black
"""

def solution(A):
    subLen = 0
    newList = []
    for i in range(len(A)):
        #print("Lenght of index: "+str(len(A[i])))
        if len(A[i]) > subLen:
            subLen = len(A[i])
            #print("SubLen = "+str(subLen))
    
    for b in range(len(A)):
        #print("Second Lenght: "+str(len(A[b])))
        #print("Len of subLen is = "+str(subLen))
        if len(A[b]) == subLen:
            #print("append")
            newList.append(A[b])
       
    #print(newList)
    return newList

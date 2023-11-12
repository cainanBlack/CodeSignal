"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
solution(text) = "steady".

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string text

Guaranteed constraints:
4 ≤ text.length ≤ 50.

[output] string

The longest word from text. It's guaranteed that there is a unique output.


Solution: Cainan Black
"""

def solution(text):    
    it = 0
    l1 = []

    for j in text:
        it += 1
        
        if j == "-":
            k = text.split("-")
            break
        elif it >= len(text):
            k = text.split(" ")  
            break
        
    for i in k:
        temp = ""
        
        for m in range(len(i)):
            if i[m].isalnum():
                temp += i[m]  
            else:
                break
                
        l1.append(temp)
                
    return max(l1, key=len)

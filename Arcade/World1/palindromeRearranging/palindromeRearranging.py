"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.


Solution: Cainan Black
"""

def solution(IS):
    odd = 0
    emp = []
    sameNum = 0
    
    print(len(IS))
    
    if len(IS) == 1:
        print("True1")
        return True
    
    if len(IS) % 2 == 0:
        for i in IS:
            emp.append(i)
        emp.sort()
        
        for o in range(len(emp)):
            try:
                if emp[o] != emp[o+1]:
                    odd += 1
                else:
                    sameNum += 1
            except Exception as e:
                print("Error: ",e)
        
        print(sameNum)        
        
        if odd >= float(((len(IS)-sameNum)/2)+.5):
            print("False2")
            return False
        else:
            print("True2")
            return True
                
    else:
        for m in IS:
            emp.append(m)
            emp.sort()
        
        for p in range(len(emp)):
            try:
                if emp[p] != emp[p+1]:
                    odd += 1
                else:
                    sameNum += 1
            except Exception as e:
                print("Error2: ",e)
            
        print(sameNum)    
            
        if odd > float(((len(IS)-sameNum)/2)+.5):
            print("False3")
            return False
        else:
            print("True3")
            return True

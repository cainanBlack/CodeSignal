"""
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be solution(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be solution(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be solution(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string inputString

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ inputString.length ≤ 50.

[output] boolean

Return true if the string is beautiful, false otherwise.


Solution: Cainan Black
"""

def solution(s1):
    dic = {}
    uniqStr = set(s1)
    uniqStr = sorted(uniqStr)
    
    if uniqStr[0] != 'a':
        return False
    
    for i in uniqStr:
        count = 0
        for b in s1:
            if i == b:
                count += 1
                dic[b] = count
                
    for k in range(len(uniqStr)-1):
        if abs(ord(uniqStr[k]) - ord(uniqStr[k+1])) != 1:
            return False
                
    for m in range(len(dic) - 1):
        if dic[uniqStr[m]] < dic[uniqStr[m + 1]]:
            return False
        
    return True

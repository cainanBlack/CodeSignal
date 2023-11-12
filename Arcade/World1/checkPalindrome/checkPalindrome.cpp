/*
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.
Input/Output

[execution time limit] 0.5 seconds (cpp)

[memory limit] 1 GB

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.


Solution: Cainan Black
*/

bool solution(string IS) {
    int i = 0; int j = int(IS.length()) - 1;
    
    while (i < j){
        if (IS[i] != IS[j]){ return false; }
        i++; j--;
    }
    
    return true;
}


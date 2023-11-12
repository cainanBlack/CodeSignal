"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;
For name = "qq-q", the output should be
solution(name) = false;
For name = "2w2", the output should be
solution(name) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string name

Guaranteed constraints:
1 ≤ name.length ≤ 10.

[output] boolean

true if name is a correct variable name, false otherwise.


Solution: Cainan Black
"""

def solution(name):
    """
    takes a string
    returns True or False
    Depending on if the input is a proper variable name or not, it returns True or False
    """
    if name[0].isdigit():
        return False
    for i in name:
        if i.isalpha() == False and i.isdigit() == False and i != '_':
            return False
    return True

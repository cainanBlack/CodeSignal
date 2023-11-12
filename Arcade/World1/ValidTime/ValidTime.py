"""
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
solution(time) = true;
For time = "25:51", the output should be
solution(time) = false;
For time = "02:76", the output should be
solution(time) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string time

A string representing time in HH:MM format. It is guaranteed that the first two characters, as well as the last two characters, are digits.

[output] boolean

true if the given representation is correct, false otherwise.


Solution: Cainan Black
"""

def solution(time):
    l1 = time.split(":")
    if 00 > int(l1[0]) or int(l1[0]) > 23:
        return False
    elif 00 > int(l1[1]) or int(l1[1]) > 59:
        return False
    else:
        return True

"""
Consider a city where the streets are perfectly laid out to form an infinite square grid. In this city finding the shortest path between two given points (an origin and a destination) is much easier than in other more complex cities. As a new Uber developer, you are tasked to create an algorithm that does this calculation.

Given user's departure and destination coordinates, each of them located on some street, find the length of the shortest route between them assuming that cars can only move along the streets. Each street can be represented as a straight line defined by the x = n or y = n formula, where n is an integer.

Example

For departure = [0.4, 1] and destination = [0.9, 3], the output should be
solution(departure, destination) = 2.7.

0.6 + 2 + 0.1 = 2.7, which is the answer.



Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.float departure

An array [x, y] of x and y coordinates. It is guaranteed that at least one coordinate is integer.

Guaranteed constraints:
0.0 ≤ departure[i] ≤ 10.0.

[input] array.float destination

An array [x, y] of x and y coordinates. It is guaranteed that at least one coordinate is integer.

Guaranteed constraints:
0.0 ≤ destination[i] ≤ 10.0.

[output] float

The shorted distance between two points along the streets.


Solution: Cainan Black
"""

def solution(departure, destination):
    if departure[0] == destination[0]:
        return abs(departure[1]-destination[1])
    elif departure[1] == destination[1]:
        return abs(departure[0]-destination[0])    
    if departure[0]!=int(departure[0]) or destination[0]!=int(destination[0]):
        print("X")
        total_ceil = 0
        x_pos_right = math.ceil(departure[0])
        total_ceil+=abs(x_pos_right-departure[0])
        total_ceil+=abs(x_pos_right-destination[0])
    
        total_floor = 0
        x_pos_left = math.floor(departure[0])
        total_floor+=abs(x_pos_left-departure[0])
        total_floor+=abs(x_pos_left-destination[0])
    
        x = min(total_ceil,total_floor)
        return x+abs(departure[1]-destination[1])
    else:
        print("Y")
        total_ceil = 0
        y_pos_right = math.ceil(departure[1])
        total_ceil+=abs(y_pos_right-departure[1])
        total_ceil+=abs(y_pos_right-destination[1])
    
        total_floor = 0
        y_pos_left = math.floor(departure[1])
        total_floor+=abs(y_pos_left-departure[1])
        total_floor+=abs(y_pos_left-destination[1])
    
        y = min(total_ceil,total_floor)
        return y+abs(departure[0]-destination[0])   

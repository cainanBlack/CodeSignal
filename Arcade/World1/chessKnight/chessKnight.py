"""
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.



Example

For cell = "a1", the output should be
solution(cell) = 2.



For cell = "c2", the output should be
solution(cell) = 6.



Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string cell

String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.

Guaranteed constraints:
cell.length = 2,
'a' ≤ cell[0] ≤ 'h',
1 ≤ cell[1] ≤ 8.

[output] integer


Solution: Cainan Black
"""

def solution(cell):
    dic = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}
    num = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8"}
    count = 0
    
    setCellKeyX = str({i for i in dic if dic[i]==cell[0]})
    setCellKeyY = str({i for i in num if num[i]==cell[1]})
    
    cellKeyX = int(setCellKeyX[1])
    cellKeyY = int(setCellKeyY[1])
    
    try:
        newX = dic[(cellKeyX)+2]
        newY = num[(cellKeyY)+1]
        count += 1
    except:
        pass
    
    try:
        newX = dic[(cellKeyX)-2]
        newY = num[(cellKeyY)+1]
        count += 1
    except:
        pass

    try:
        newX = dic[(cellKeyX)+2]
        newY = num[(cellKeyY)-1]
        count += 1
    except:
        pass
    
    try:
        newX = dic[(cellKeyX)-2]
        newY = num[(cellKeyY)-1]
        count += 1
    except:
        pass
    
    try:
        newX = dic[(cellKeyX)+1]
        newY = num[(cellKeyY)+2]
        count += 1
    except:
        pass
    
    try:
        newX = dic[(cellKeyX)-1]
        newY = num[(cellKeyY)+2]
        count += 1
    except:
        pass
        
    try:
        newX = dic[(cellKeyX)+1]
        newY = num[(cellKeyY)-2]
        count += 1
    except:
        pass
    
    try:
        newX = dic[(cellKeyX)-1]
        newY = num[(cellKeyY)-2]
        count += 1
    except:
        pass
    
    return count

/*
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 0.5 seconds (cpp)

[memory limit] 1 GB

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.


Solution: Cainan Black
*/

vector<string> solution(vector<string> ia) {
    int longList = 0;
    int amount = 0;
    
    for(int i = 0; i < ia.size(); i++) {
        if(ia[i].length() > longList){
            longList = int(ia[i].length());
            amount = 0;
        } else if (ia[i].length() == longList){
            amount++;
        }
    }
    
    vector <string> resList;
    amount = 0;
    
    for(int c = 0; c < ia.size(); c++){
        if(ia[c].length() == longList){
            resList.push_back(ia[c]);
            amount++;
        }
    }
    return resList;
}

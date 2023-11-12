/*
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 0.5 seconds (cpp)

[memory limit] 1 GB

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.


Solution: Cainan Black
*/

int solution(vector<int> ia) {
    int topval = ia[0] * ia[1];
    
    for(int i = 1; i < ia.size(); i ++){
        if(ia[i] * ia[i-1] > topval){
            topval = ia[i] * ia[i-1];
        }
    }
    return topval;
}

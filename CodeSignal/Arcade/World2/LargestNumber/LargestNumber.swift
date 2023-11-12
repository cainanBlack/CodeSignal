//Example
//
//For n = 2, the output should be
//solution(n) = 99.
//
//Input/Output
//
//[execution time limit] 6 seconds (swift)
//
//[memory limit] 1 GB
//
//[input] integer n
//
//Guaranteed constraints:
//1 ≤ n ≤ 9.
//
//[output] integer
//
//The largest integer of length n.
//
//
//Solution: Cainan Black


func solution(n: Int) -> Int {
    return Int(pow(10.0, Double(n))) - 1
}

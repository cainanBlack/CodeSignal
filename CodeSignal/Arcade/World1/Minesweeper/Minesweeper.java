/*
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]
Check out the image below for better understanding:



Input/Output

[execution time limit] 3 seconds (java)

[memory limit] 1 GB

[input] array.array.boolean matrix

A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell contains a mine, false otherwise.

Guaranteed constraints:
2 ≤ matrix.length ≤ 100,
2 ≤ matrix[0].length ≤ 100.

[output] array.array.integer

Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.


Solution: Cainan Black
*/

int[][] solution(boolean[][] matrix) {

    int[][] sol = new int[matrix.length][matrix[0].length];
    for (int i = 0; i < matrix.length; i++)
        for (int j = 0; j < matrix[0].length; j++)
            for (int ii = Math.max(0,i - 1); ii <= Math.min(i + 1,matrix.length-1) ; ii++)
                for (int jj = Math.max(0,j - 1); jj <= Math.min(j + 1,matrix[0].length-1); jj++) {
                    if (matrix[ii][jj] && (i!=ii || jj!=j)) {
                        sol[i][j]++;                        
                    }
                }
    return sol;   
}

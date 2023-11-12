/*
After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).


Solution: Cainan Black
*/

int solution(vector<vector<int>> m) {
    int row = m.size();
    int col = m[0].size();
    int res = 0;
    
    for(int c = 0; c < col; c++){
        for(int r = 0; r < row; r++){
            if(m[r][c] != 0){
                res += m[r][c];
            } else {
                break;
            }
        }
    }
    return res;
    
}

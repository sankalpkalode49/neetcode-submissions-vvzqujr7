class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std:: unordered_map<char, int> rows[9];
        std:: unordered_map<char, int> cols[9];
        std:: unordered_map<char, int> boxes[9];

        for (int i = 0; i <9; i++){
            for (int j = 0; j < board.size(); j++){
                char c = board[i][j];
                if (c != '.'){
                    if (rows[i][c]++ > 0) return false;
                    if (cols[j][c]++ > 0) return false;
                    int boxIndex = (i / 3) * 3 + j / 3;
                    if (boxes[boxIndex][c]++ > 0) return false;
                }


            }
        }
        return true;

        
    }
};

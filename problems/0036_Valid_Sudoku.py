class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            hm = {}
            for j in range(9):
                if board[i][j] in hm.keys() and board[i][j]!=".":
                    return False
                else:
                    hm[board[i][j]]=1
        
        for i in range(9):
            hm = {}
            for j in range(9):
                if board[j][i] in hm.keys() and board[j][i]!=".":
                    return False
                else:
                    hm[board[j][i]]=1
        
        for i in range(3):
            for j in range(3):
                hm = {}
                for k in range(i*3,(i+1)*3):
                    for l in range(j*3,(j+1)*3):
                        if board[k][l] in hm.keys() and board[k][l]!=".":
                            return False
                        else:
                            hm[board[k][l]]=1
        return True
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
c = Solution()
print(c.isValidSudoku(board))
            
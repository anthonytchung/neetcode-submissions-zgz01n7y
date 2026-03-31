class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        found = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in found:
                        return False
                    else:
                        found[board[i][j]] = 0
            found.clear()

            for j in range(len(board[i])):
                if board[j][i] != ".":
                    if board[j][i] in found:
                        return False
                    else:
                        found[board[j][i]] = 0
            found.clear()
        
        #squares now
        for square in range(9):
            for i in range(0, 3):
                for j in range(0, 3):
                    if board[i][j] != ".":
                        if board[i][j] in found:
                            return False
                        else:
                            found[board[i][j]] = 0
            found.clear()

        return True
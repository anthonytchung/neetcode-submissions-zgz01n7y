class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                key = ((r // 3), (c // 3))
                val = board[r][c]
                if not val.isalnum():
                    continue
                if val in row[r] or val in col[c] or val in square[key]:
                    return False
                else:
                    row[r].add(val)
                    col[c].add(val)
                    square[key].add(val)
            

        return True
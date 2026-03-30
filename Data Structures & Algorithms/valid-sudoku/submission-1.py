class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = 9

        # first condition - rows
        for i in range(n):
            row = set()
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    continue
                if val in row:
                    return False
                row.add(val)

        # second condition - columns
        for i in range(n):
            col = set()
            for j in range(n):
                val = board[j][i]
                if val == ".":
                    continue
                if val in col:
                    return False
                col.add(val)

        # third condition - sub-boxes
        for i in range(n):
            sq = set()
            for j in range(3):
                for k in range(3):
                    row = (i // 3) * 3 + j
                    col = (i % 3) * 3 + k
                    val = board[row][col]
                    if val == ".":
                        continue
                    if val in sq:
                        return False
                    sq.add(val)

        return True
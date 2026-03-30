class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        def dfs(row, col, index):

            if index == len(word):
                return True

            if row < 0 or row == len(board) or col < 0 or col == len(board[0]):
                return False

            if board[row][col] != word[index] or (row, col) in visited:
                return False

            visited.add((row, col))
            # 4 possible moves from any given cell
            if dfs(row+1, col, index+1) or dfs(row-1, col, index+1) or dfs(row, col+1, index+1) or dfs(row, col-1, index+1):
                return True
            visited.remove((row, col))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0):
                    return True
        
        return False
        
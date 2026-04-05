class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(row, col):
            
            if row < 0 or row == rows or col < 0 or col == cols or (row, col) in visited or grid[row][col] == 0:
                return 0
            
            visited.add((row, col))
            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, dfs(r, c))
        
        return res
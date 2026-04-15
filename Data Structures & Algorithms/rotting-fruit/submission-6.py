class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))

        while q:
            n = len(q)
            for i in range(n):
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row+dr, col+dc
                    if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
            if len(q) > 0:
                res += 1
        
        if any(1 in row for row in grid):
            return -1
        return res
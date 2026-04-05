class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()

        # [1,-1,0,1],
        # [1,1,1,-1],
        # [1,-1,1,-1],
        # [0,-1,1,1]'

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                new_row, new_col = r+dr, c+dc

                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == INF:
                    grid[new_row][new_col] = grid[r][c] + 1
                    q.append((new_row, new_col))
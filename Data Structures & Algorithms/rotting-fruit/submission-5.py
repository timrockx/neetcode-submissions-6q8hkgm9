class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        time=0
        while q:
            old_size = len(q)
            for _ in range(old_size):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc  
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        visited.add((new_row, new_col))
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
            if len(q) > 0:
                time += 1
        
        if any(1 in row for row in grid):
            return -1
        return time


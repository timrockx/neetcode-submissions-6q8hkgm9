class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # for r in range(rows):
        #     for c in range(cols):
        #         if (r, c) not in visited and grid[r][c] == 1:
        #             q = deque()
        #             q.append((r, c))
        #             visited.add((r, c))
        #             area = 0
        #             while q:
        #                 row, col = q.popleft()
        #                 area += 1
        #                 for dr, dc in directions:
        #                     new_row, new_col = row + dr, col + dc
        #                     if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:                                
        #                         q.append((new_row, new_col))
        #                         visited.add((new_row, new_col))
        #             res = max(res, area)
        
        # return res
        def dfs(row, col):                        
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] == 0:
                return 0
            
            visited.add((row, col))        
            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)            

        for r in range(rows):
            for c in range(cols):
                # if (r, c) not in visited and grid[r][c] == 1:
                res = max(res, dfs(r, c))
        
        return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        res = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # def dfs(row, col):
        #     if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] == "0":
        #         return

        #     visited.add((row, col))
        #     dfs(row+1, col)
        #     dfs(row-1, col)
        #     dfs(row, col+1)
        #     dfs(row, col-1)

        # for r in range(rows):
        #     for c in range(cols):
        #         if (r, c) not in visited and grid[r][c] == "1":                    
        #             dfs(r, c)
        #             res += 1

        def bfs(row, col):
            visited.add((row, col))
            q = deque()
            q.append((row, col))            

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc

                    if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and grid[new_row][new_col] == "1":
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":                    
                    bfs(r, c)
                    res += 1
                
        return res



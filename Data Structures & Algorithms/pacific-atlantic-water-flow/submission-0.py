class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        res = []
        pacific, atlantic = set(), set()

        def dfs(row, col, visited, prev):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or heights[row][col] < prev:
                return
            
            visited.add((row, col))
            dfs(row+1, col, visited, heights[row][col])
            dfs(row-1, col, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col]) 

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    dfs(r, c, pacific, 0)
        
        for r in range(rows):
            for c in range(cols):
                if r == rows-1 or c == cols-1:
                    dfs(r, c, atlantic, 0)
        
        for row, col in list(pacific&atlantic):
            res.append([row, col])
        
        print(res)

        return res
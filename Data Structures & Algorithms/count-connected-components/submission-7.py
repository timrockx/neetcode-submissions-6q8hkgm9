class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_map = defaultdict(list)
        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)
    
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for n in adj_map[i]:
                dfs(n)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res

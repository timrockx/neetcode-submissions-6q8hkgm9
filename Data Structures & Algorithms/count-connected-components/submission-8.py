class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_map = defaultdict(list)
        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for n in adj_map[node]:
                dfs(n)

        connected = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected += 1

        return connected

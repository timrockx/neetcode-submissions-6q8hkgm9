class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_map = defaultdict(list)
        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)
        
        print(adj_map)

        visited = set()
        def dfs(i, parent):
            
            if i in visited:
                return False
            visited.add(i)

            for n in adj_map[i]:
                if n == parent:
                    continue
                if not dfs(n, i):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
        
        

            


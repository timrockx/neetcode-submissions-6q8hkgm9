class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_map = defaultdict(list)
        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)
        
        q = deque()
        visited = set()
        res = 0

        for i in range(n):

            if i not in visited:
                q.append(i)
                visited.add(i)
                res += 1

                while q:
                    node = q.popleft()
                    for adj in adj_map[node]:
                        if adj not in visited:
                            visited.add(adj)
                            q.append(adj)
        
        return res
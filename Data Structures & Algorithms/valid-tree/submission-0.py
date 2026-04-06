class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        adj_map = defaultdict(list)

        for first, second in edges:
            adj_map[first].append(second)
            adj_map[second].append(first)

        q = deque([0])
        visited = set()

        while q:
            val = q.popleft()
            if val in visited:
                continue
            visited.add(val)
            for node in adj_map[val]:
                q.append(node)
        
        return len(visited) == n

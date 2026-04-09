class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parents = list(range(n))
        rank = [0] * n

        def find(x):
            if parents[x] != x:
                return find(parents[x])
            return parents[x]

        edges.sort()
        for a, b in edges:
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                if rank[root_a] > rank[root_b]:
                    parents[root_b] = root_a
                elif rank[root_b] > rank[root_a]:
                    parents[root_a] = root_b
                else:
                    parents[root_a] = root_b
                    rank[root_b] += 1
                n -= 1

        return n



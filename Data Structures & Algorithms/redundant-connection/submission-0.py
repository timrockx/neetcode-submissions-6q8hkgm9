class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parents = list(range(len(edges)+1))
        rank = [0] * (len(edges) + 1)
        print(parents, rank)

        def find(x):
            print(x)
            if parents[x] != x:
                return find(parents[x])
            return parents[x]

        for a, b in edges:
            print([a, b])
            parent_a, parent_b = find(a), find(b)
            print(parent_a, parent_b)

            if parent_a != parent_b:

                if rank[parent_a] > rank[parent_b]:
                    parents[parent_b] = parent_a
                
                elif rank[parent_b] > rank[parent_a]:
                    parents[parent_a] = parent_b

                else:
                    parents[parent_a] = parent_b
                    rank[parent_b] += 1
            
            else:
                return [a, b]

        return [-1, -1]

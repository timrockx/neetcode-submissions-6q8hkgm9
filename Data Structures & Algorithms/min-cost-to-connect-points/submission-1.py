class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        costs = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                costs.append((dist, i, j))
        costs.sort()

        parents = [x for x in range(len(points))]
        rank = [0] * len(points)
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        res = 0
        seen = set()
        for cost, u, v in costs:

            parent_u, parent_v = find(u), find(v)
            if parent_u == parent_v:
                continue

            res += cost
            if rank[parent_u] > rank[parent_v]:
                parents[parent_v] = parent_u
            elif rank[parent_v] > rank[parent_u]:
                parents[parent_u] = parent_v
            else:
                parents[parent_v] = parent_u
                rank[parent_v] += 1

        return res


            
            

        



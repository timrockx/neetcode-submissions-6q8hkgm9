import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj_map = defaultdict(list)
        idx = 0
        for a, b in edges:
            adj_map[a].append((b, succProb[idx]))
            adj_map[b].append((a, succProb[idx]))
            idx += 1
                
        # want to store highest probability
        max_heap = [(-1, start_node)]
        visited = set()

        while max_heap:
            prob, node = heapq.heappop(max_heap)
            if node in visited:
                continue
            visited.add(node)

            if node == end_node:
                return -prob

            for n, p in adj_map[node]:
                if n not in visited:
                    heapq.heappush(max_heap, (prob * p, n))

        return 0




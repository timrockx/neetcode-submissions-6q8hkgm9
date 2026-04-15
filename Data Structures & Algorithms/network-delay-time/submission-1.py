import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_map = defaultdict(list)
        for src, tgt, t in times:
            adj_map[src].append((tgt, t))
        
        min_heap = [(0, k)]
        visited = set()
        t = 0
        while min_heap:
            curr_distance, curr = heapq.heappop(min_heap)
            if curr in visited:
                continue
            visited.add(curr)
            t = curr_distance

            for neighbor, weight in adj_map[curr]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (curr_distance + weight, neighbor))
        
        return t if len(visited) == n else -1
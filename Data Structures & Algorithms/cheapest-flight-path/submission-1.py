import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj_map = defaultdict(list)
        for start, dest, cost in flights:
            adj_map[start].append((dest, cost))

        min_heap = [(0, 0, src)]

        while min_heap:
            print(min_heap)
            cost, stops, node = heapq.heappop(min_heap)
            
            if stops > k+1:
                continue

            if node == dst and stops <= k+1:
                return cost
            stops += 1
            
            for dest, c in adj_map[node]:
                heapq.heappush(min_heap, (cost+c, stops, dest))

        return -1

            

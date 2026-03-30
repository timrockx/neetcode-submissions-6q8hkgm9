import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            print(max_heap)
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if x < y:
                heapq.heappush(max_heap, -1*(y-x))
        
        print(max_heap)
        return abs(heapq.heappop(max_heap)) if max_heap else 0

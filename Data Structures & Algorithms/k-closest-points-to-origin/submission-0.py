import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []

        for point in points:
            distance = (point[0]**2 + point[1]**2)**0.5
            heapq.heappush(min_heap, [distance, point])

        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res
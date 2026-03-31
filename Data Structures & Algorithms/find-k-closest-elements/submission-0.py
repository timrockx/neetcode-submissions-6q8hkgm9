import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        res = []
        min_heap = []

        for i in range(len(arr)):
            dist = abs(arr[i] - x)
            heapq.heappush(min_heap, (dist, i))
        
        while len(res) < k:
            dist, idx = heapq.heappop(min_heap)
            res.append(arr[idx])
        
        res.sort()
        return res



        # calculate distance for each element
        # if we are < k integers, then we can just add it
        # if we are > k integers, then compare distance
        # if distance is == at any point, we retain the earliest value (always will be less)

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = [-x for x in nums]
        heapq.heapify(self.max_heap)
        self.k = k

    def add(self, val: int) -> int:
        
        heapq.heappush(self.max_heap, -1*val)
        temp_heap = list(self.max_heap)
        print(temp_heap)
        for i in range(self.k-1):
            x = heapq.heappop(temp_heap)
            print(x)
        
        return heapq.heappop(temp_heap) * -1


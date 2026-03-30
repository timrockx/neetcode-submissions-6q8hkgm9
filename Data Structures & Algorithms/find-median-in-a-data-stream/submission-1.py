class MedianFinder:

    def __init__(self):
        self.small_half = []
        self.large_half = []
        self.length = 0

    def addNum(self, num: int) -> None:
        
        if self.large_half and num > self.large_half[0]:
            heapq.heappush(self.large_half, num)
        else:
            heapq.heappush(self.small_half, -1 * num)

        if len(self.small_half) > len(self.large_half) + 1:
            val = -1 * heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, val)
        if len(self.large_half) > len(self.small_half) + 1:
            val = -1 * heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, val)
        
        self.length += 1

    def findMedian(self) -> float:

        if self.length % 2 == 0:
            median = ((-1*self.small_half[0]) + self.large_half[0]) / 2.0
            return median
        else:
            if len(self.small_half) > len(self.large_half):
                return -1*self.small_half[0]
            return self.large_half[0]
            

        
        
import heapq
class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []        

    def addNum(self, num: int) -> None:

        if self.right_heap and num > self.right_heap[0]:
            heapq.heappush(self.right_heap, num)
        else:
            heapq.heappush(self.left_heap, -1*num)

        if len(self.right_heap) - len(self.left_heap) > 1:
            x = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -1*x)
        
        if len(self.left_heap) - len(self.right_heap) > 1:
            x = heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, -1*x)

    def findMedian(self) -> float:
        print(self.left_heap, self.right_heap)

        if len(self.right_heap) > len(self.left_heap):
            return self.right_heap[0]
        if len(self.left_heap) > len(self.right_heap):
            return -1*self.left_heap[0]
        return (-1*self.left_heap[0] + self.right_heap[0]) / 2.0
        
        
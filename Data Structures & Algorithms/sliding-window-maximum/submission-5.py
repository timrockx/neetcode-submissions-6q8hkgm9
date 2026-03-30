import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 0
        res = []

        for i in range(len(nums)+1):

            if i - left == k:
                window = [-num for num in nums[left:i]]
                heapq.heapify(window)                
                res.append(-1*heapq.heappop(window))
                left += 1

        return res

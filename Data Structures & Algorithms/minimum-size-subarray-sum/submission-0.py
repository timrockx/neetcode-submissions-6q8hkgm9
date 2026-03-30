class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = float('inf')

        left, cur = 0, 0

        for i in range(len(nums)):

            cur += nums[i]

            while cur >= target:
                res = min(res, i - left + 1)
                cur -= nums[left]
                left += 1
        
        return 0 if res == float('inf') else res

            
            
                

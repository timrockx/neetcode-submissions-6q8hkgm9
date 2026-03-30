class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float('-inf')
        curr = 0
        for n in nums:
            
            if n > curr + n:
                curr = n
            else:
                curr += n
            
            res = max(res, curr)

        return res
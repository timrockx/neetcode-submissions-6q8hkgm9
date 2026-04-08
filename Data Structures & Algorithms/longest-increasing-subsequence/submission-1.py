import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        res = [ nums[0] ]

        for i in range(1, len(nums)):

            idx = bisect.bisect_left(res, nums[i])
            if idx < len(res):
                res[idx] = nums[i]
            else:
                res.append(nums[i])
            print(res, idx, nums[i])
        

        return len(res)

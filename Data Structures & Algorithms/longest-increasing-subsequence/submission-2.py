import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        res = [ nums[0] ]

        for i in range(1, len(nums)):

            idx = bisect.bisect_left(res, nums[i])
            if idx < len(res):
                # fits somewhere in the existing LIS - we can replace the value
                # since the length is not changing, and taking a lower # at any 
                # point is always ideal for any future longer subsequences
                res[idx] = nums[i]
            else:
                # greater than all
                res.append(nums[i])

        return len(res)

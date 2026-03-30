class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        res = 0
        def backtrack(i, curr_sum):
            nonlocal res

            if i == len(nums) and curr_sum == target:
                res += 1
                return

            if i == len(nums):
                return
            
            backtrack(i+1, curr_sum + nums[i])
            backtrack(i+1, curr_sum - nums[i])

        backtrack(0, 0)
        return res


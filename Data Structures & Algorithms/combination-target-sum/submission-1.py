class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []

        def dfs(i, curr_sum):

            if curr_sum == target:
                res.append(curr.copy())
                return
            if curr_sum > target or i >= len(nums):
                return

            curr_sum += nums[i]
            curr.append(nums[i])
            dfs(i, curr_sum)
            curr.pop()
            curr_sum -= nums[i]
            dfs(i + 1, curr_sum)

        dfs(0, 0)    
        return res
        
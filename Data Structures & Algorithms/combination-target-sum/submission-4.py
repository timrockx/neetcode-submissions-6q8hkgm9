class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        cur = []
        nums.sort()

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(cur.copy())
                return

            if curr_sum > target or i == len(nums):
                return

            curr_sum += nums[i]
            cur.append(nums[i])
            dfs(i, curr_sum)
            cur.pop()
            curr_sum -= nums[i]

            dfs(i+1, curr_sum)

        dfs(0, 0)
        return res
            

            

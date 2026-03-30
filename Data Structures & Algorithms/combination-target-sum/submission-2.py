class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []

        def dfs(i, curr_sum):

            if curr_sum == target:
                    res.append(curr.copy())
                    return

            for j in range(i, len(nums)):

                if curr_sum > target:            
                    break

                curr_sum += nums[j]
                curr.append(nums[j])
                # go deeper on same element
                dfs(j, curr_sum)
                curr.pop()
                curr_sum -= nums[j]

        dfs(0, 0)    
        return res
        
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []

        def dfs(i, curr_sum):
            print(f"new dfs(), at {i}, with {curr_sum}")

            for j in range(i, len(nums)):

                if curr_sum > target:            
                    break

                if curr_sum == target:
                    print(curr, curr_sum)
                    res.append(curr.copy())
                    return

                curr_sum += nums[j]
                curr.append(nums[j])
                # go deeper on same element
                dfs(j, curr_sum)
                curr.pop()
                curr_sum -= nums[j]

        dfs(0, 0)    
        return res
        
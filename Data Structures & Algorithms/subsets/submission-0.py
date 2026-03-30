class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(index):

            # base case, hand
            if index == len(nums):
                res.append(curr.copy())
                return

            # include nums[i]
            curr.append(nums[index])
            dfs(index+1)
            curr.pop()

            # skip nums[i]
            dfs(index+1)

        dfs(0)
        return res

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        curr = []

        def dfs(i):

            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i+1)
            curr.pop()

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[i]:
                    i += 1
                
            dfs(i+1)

        dfs(0)
        return res



        

        
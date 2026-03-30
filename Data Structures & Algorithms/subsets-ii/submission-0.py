class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        res = []
        curr = []

        def dfs(i):

            if i >= len(nums):
                if curr.copy() in res:
                    return
                res.append(curr.copy())
                return
            
            # if i > 0 and nums[i] == nums[i-1]:
            #     return

            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)
        
        dfs(0)
        return res


        
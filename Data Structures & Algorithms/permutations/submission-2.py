class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res, cur = [], []
        visited = [False] * len(nums)

        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):

                if not visited[i]:
                    visited[i] = True
                    cur.append(nums[i])
                    dfs()
                    cur.pop()
                    visited[i] = False
                else:
                    continue
        dfs()
        return res
                
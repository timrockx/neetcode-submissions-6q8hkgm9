class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        cur = []
        visited = [False] * len(nums)

        def dfs():

            if len(cur) == len(nums):
                res.add(tuple(cur.copy()))
                return

            for i in range(len(nums)):

                if not visited[i]:
                    cur.append(nums[i])
                    visited[i] = True
                    dfs()
                    cur.pop()
                    visited[i] = False
            
        dfs()
        return [list(perm) for perm in list(res)]
            
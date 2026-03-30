class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        cur = []
        nums.sort()
        visited = [False] * len(nums)

        def dfs():

            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(nums)):

                if visited[i]:
                    continue

                if i>0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                cur.append(nums[i])
                visited[i] = True
                dfs()
                cur.pop()
                visited[i] = False
            
        dfs()
        return res
            
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        nums.sort()

        def dfs(i, cur):

            if cur == target:
                return True
            
            if i == len(nums):
                return False
            
            if cur + nums[i] > target:
                return False
            
            return dfs(i+1, cur+nums[i]) or dfs(i+1, cur)
        
        return dfs(0, 0)

        # [1, 2, 3, 4] target = 5

        1 

        1 + 2
            

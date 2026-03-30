class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k
        visited = [False] * len(nums)

        def backtrack(i, k, curr_sum):

            if k == 0:
                return True

            if curr_sum == target:
                return backtrack(0, k-1, 0)

            for j in range(i, len(nums)):
                if nums[j] + curr_sum <= target and not visited[j]:
                    visited[j] = True
                    if backtrack(j+1, k, curr_sum + nums[j]):
                        return True
                    visited[j] = False
            return False

        return backtrack(0, k, 0)

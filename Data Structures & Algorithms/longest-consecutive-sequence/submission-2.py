class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        unique = set(nums)
        sorted_nums = sorted(unique)

        res = 0
        curr = 1

        for i in range(1, len(sorted_nums)):

            if sorted_nums[i] == sorted_nums[i-1] + 1:
                curr += 1

            else:
                res = max(res, curr)
                curr = 1
        
        return max(res, curr)

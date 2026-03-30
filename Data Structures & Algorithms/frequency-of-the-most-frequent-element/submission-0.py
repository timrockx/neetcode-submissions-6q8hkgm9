class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        left, res = 0, 0
        nums.sort()

        for i in range(len(nums)):

            window = nums[left:i+1]
            if nums[i] * len(window) - sum(window) > k:
                left += 1
            else:
                res = max(res, i - left + 1)

        return res
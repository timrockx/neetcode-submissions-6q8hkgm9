class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        res = 0
        left = 0
        cur = 1
        for i in range(len(nums)):

            cur *= nums[i]

            while cur >= k and left <= i:

                cur //= nums[left]
                left += 1

            res += (i - left + 1)
        
        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        unique = sorted(vals)

        res = 0
        start = 0

        for i in range(len(unique)):
            if unique[i] - 1 not in vals:
                start = i
            
            res = max(res, i - start + 1)  # fix 2: update every iteration, not just in else

        return res
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] >= 2:
                return num

        return [key for key, val in count.items() if val >= 2]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff = {}

        for i in range(len(nums)):

            difference = target - nums[i]

            if difference in diff:
                idx = diff[difference]
                return [idx, i]

            diff[nums[i]] = i
        
        return [0, 0]
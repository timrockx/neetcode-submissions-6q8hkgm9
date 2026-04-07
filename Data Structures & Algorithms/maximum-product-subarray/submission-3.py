class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_product = 1
        min_product = 1
        res = nums[0]

        for i in range(len(nums)):
            temp = max_product
            max_product = max(max_product*nums[i], min_product*nums[i], nums[i])
            min_product = min(temp*nums[i], min_product*nums[i], nums[i])
            res = max(res, max_product)
        
        return res  
        
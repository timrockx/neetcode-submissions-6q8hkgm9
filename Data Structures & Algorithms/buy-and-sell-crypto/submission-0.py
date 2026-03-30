class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        res = 0

        for right in range(len(prices)):

            if prices[right] > prices[left]:
                res = max(res, prices[right] - prices[left])
            else:
                left = right
            
        return res
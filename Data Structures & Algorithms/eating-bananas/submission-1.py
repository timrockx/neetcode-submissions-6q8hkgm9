import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        res = max(piles)
        left, right = 1, max(piles)

        while left <= right:

            mid = (left + right) // 2

            t = 0
            for pile in piles:
                t += math.ceil( pile / mid )

            if t > h:
                left = mid + 1

            if t <= h:
                res = min(res, mid)
                right = mid - 1
        
        return res
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res, pfix = 0, 0
        tbl = defaultdict(int)

        for num in nums:

            tbl[pfix] += 1
            pfix += num
            res += tbl[pfix - k]
        
        return res
            
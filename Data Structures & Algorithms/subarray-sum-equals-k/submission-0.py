class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        prefix = 0
        tbl = defaultdict(int)
        tbl[0] = 1

        for i in range(len(nums)):
            prefix += nums[i]

            if prefix - k in tbl:
                res += tbl[prefix-k]
            
            tbl[prefix] += 1          
            
        return res

            
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        cur = 0
        res = -1
        if sum(cost) > sum(gas):
            return res

        res = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                res = i+1
            
        return res
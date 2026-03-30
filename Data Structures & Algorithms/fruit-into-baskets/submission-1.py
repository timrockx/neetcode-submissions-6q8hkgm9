class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        types = defaultdict(int)
        res = 0
        left = 0

        for i in range(len(fruits)):

            types[fruits[i]] += 1

            while len(types) > 2:
                to_remove = fruits[left]
                types[to_remove] -= 1
                if not types[to_remove]:
                    del types[to_remove]
                left += 1

            res = max(res, i - left + 1)
        
        return res
            
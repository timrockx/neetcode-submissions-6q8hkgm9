class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        left = 0
        max_count = 0
        res = 0

        for i in range(len(s)):

            count[s[i]] = count.get(s[i], 0) + 1
            max_count = max(max_count, count[s[i]])

            if (i - left + 1) - max_count > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            res = max(res, i - left + 1)
            
            
        return res



        

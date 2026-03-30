class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = set()
        left = 0
        res = 0
        for i in range(len(s)):

            while s[i] in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(s[i])                
            res = max(res, i - left + 1)

        return res


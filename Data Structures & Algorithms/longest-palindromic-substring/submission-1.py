class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_center(s, left, right):
            pali = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                pali = s[left: right+1]
                left -= 1
                right += 1
            
            return pali

        res = ""
        for i in range(len(s)):
            even = expand_center(s, i, i+1)
            odd = expand_center(s, i, i)
            
            if len(even) > len(odd) and len(even) > len(res):
                res = even
            elif len(odd) > len(even) and len(odd) > len(res):
                res = odd

        return res

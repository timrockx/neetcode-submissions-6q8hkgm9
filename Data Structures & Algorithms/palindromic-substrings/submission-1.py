class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        
        def expand(s, left, right):
            res = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            return res
                
        for i in range(len(s)):
            # even
            res += expand(s, i, i+1)
            # odd
            res += expand(s, i, i)

        return res




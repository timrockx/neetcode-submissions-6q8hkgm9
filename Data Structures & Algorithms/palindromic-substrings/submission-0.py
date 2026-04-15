class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        
        def expand(s, left, right):
            nonlocal res
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                    
                    res += 1
                else:
                    return

        
        for i in range(len(s)):
            # each character on its own is a palindrome
            res += 1
            # even
            expand(s, i, i+1)
            # odd
            expand(s, i-1, i+1)

        return res




class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_center(s, left, right):
            pali = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                pali = s[left: right+1]
                left -= 1
                right += 1            
            return pali, right - left + 1

        res, longest = "", 0
        for i in range(len(s)):
            even, e_len = expand_center(s, i, i+1)
            odd, o_len = expand_center(s, i, i)
            
            if e_len > o_len and e_len > longest:
                res = even
                longest = e_len
            elif o_len > e_len and o_len > longest:
                res = odd
                longest = o_len
        return res

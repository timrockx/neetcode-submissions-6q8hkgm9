from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # use Counter to create dict of the substrings
        s_count = Counter(s)
        t_count = Counter(t)
        res = ""
        len_res = float('inf')

        if t_count > s_count:
            return res

        l = 0
        
        for r in range(len(t), len(s)+1):
            substr = s[l:r]
            print(substr)
                    
            while t_count <= Counter(s[l:r]):
                if len(s[l:r]) < len_res:
                    len_res = len(s[l:r])
                    res = s[l:r]
                l += 1

        return res
                

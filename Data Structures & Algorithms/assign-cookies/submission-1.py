class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        res = 0
        

        for i in range(len(g)):

            for j in range(len(s)):

                if s[j] >= g[i]:
                    g[i] = float('inf')
                    s[j] -= g[i]
                    res += 1
        
        return res

class Solution:

    def is_pali(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        cur = []

        def dfs(i):

            if i == len(s):
                res.append(cur.copy())
                return

            for j in range(i, len(s)):
                if self.is_pali(s[i:j+1]):
                    cur.append(s[i:j+1])
                    dfs(j+1)
                    cur.pop()
            

        dfs(0)
        return res
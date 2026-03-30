class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        cur = []

        def backtrack(i):

            if len(cur) == k:
                res.append(cur.copy())
                return

            for j in range(i, n+1):
                cur.append(j)
                backtrack(j+1)
                cur.pop()
        
        backtrack(1)
        return res
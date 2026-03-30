class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        cur = []

        def dfs(i):

            if len(cur) == 4 and i == len(s):
                res.append(".".join(cur))
                return
            
            if len(cur) == 4 or i == len(s):
                return

            for j in range(1, 4):

                if i + j > len(s):
                    break

                segment = s[i: i + j]
                if len(segment) > 1 and segment[0] == "0":
                    continue
                if int(segment) < 0 or int(segment) > 255:
                    continue

                cur.append(segment)
                dfs(i+j)
                cur.pop()
        
        dfs(0)
        return res



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(op, cl, cur):
            if cl > op:
                return

            if len(cur) == n * 2 and op == cl:
                res.append(cur)
                return
            
            if op < n:
                backtrack(op+1, cl, cur+"(")
            
            if cl < op:
                backtrack(op, cl+1, cur+")")

        backtrack(0, 0, "")
        return res
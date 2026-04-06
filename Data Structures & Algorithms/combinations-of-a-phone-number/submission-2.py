class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []
        def backtrack(cur, i):
            if len(cur) == len(digits):
                res.append(cur)
                return
            
            for char in mapping[digits[i]]:
                backtrack(cur+char, i+1)
            

        if not digits:
            return []
        backtrack("", 0)
        return res

        


        

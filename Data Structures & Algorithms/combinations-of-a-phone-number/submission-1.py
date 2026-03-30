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
        res = [] if not digits else [""]

        for d in digits:
            tmp = []
            for curr in res:
                for char in mapping[d]:
                    tmp.append(curr + char)
            res = tmp
        return res


        

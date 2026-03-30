class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left_stack = []
        star_stack = []

        for i in range(len(s)):
            char = s[i]
            if char == "*":
                star_stack.append(i)
            elif char == "(":
                left_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:                    
                    star_stack.pop()
                else:
                    return False
        
        while left_stack and star_stack:

            left_idx = left_stack.pop()
            star_idx = star_stack.pop()

            if left_idx > star_idx:
                return False
        
        if left_stack:
            return False
        
        return True

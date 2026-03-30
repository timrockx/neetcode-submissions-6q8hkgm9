class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1
        replaced = 1

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # right+1 for the bounds
                skip_left = s[left+1:right+1]
                # leave right for bounds
                skip_right = s[left:right]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
                    
        return True

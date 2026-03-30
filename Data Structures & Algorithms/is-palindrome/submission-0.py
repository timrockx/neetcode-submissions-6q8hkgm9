class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        converted = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        left, right = 0, len(converted) - 1

        while left <= right:

            if converted[left] == converted[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
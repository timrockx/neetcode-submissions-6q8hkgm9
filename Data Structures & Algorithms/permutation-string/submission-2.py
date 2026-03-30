from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = Counter(s1)
        left = 0

        for i in range(0, len(s2)):
            if ((i - left + 1) == len(s1)):
                s2_count = Counter(s2[left:i+1]) 

                if s1_count == s2_count:
                    return True
                else:
                    left += 1

        return False
        

            



            
import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()

        count = collections.Counter(hand)
        print(count)
        while len(count) != 0:
            
            start = min(count)
            print(start, count)

            for i in range(start, start+groupSize):
                if i in count:
                    count[i] -= 1
                    if count[i] == 0:
                        del count[i]                    
                else:
                    return False


        return True
        
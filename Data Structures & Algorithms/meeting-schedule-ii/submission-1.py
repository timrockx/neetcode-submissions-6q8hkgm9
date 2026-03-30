"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])

        left, right = 0, 0
        count, res = 0, 0

        while left < len(start) and right < len(end):

            if start[left] < end[right]:
                count += 1
                res = max(res, count)
                left += 1
            else:
                right += 1
                count -= 1
        
        return res
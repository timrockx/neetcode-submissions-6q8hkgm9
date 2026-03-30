"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sorted_int = sorted(intervals, key=lambda interval: interval.start)

        if len(sorted_int) <= 1:
            return True

        if len(sorted_int) == 2:
            if sorted_int[0].end <= sorted_int[1].start:
                return True
            else:
                return False

        for i in range(1, len(sorted_int) - 1):

            if sorted_int[i].start >= sorted_int[i-1].end and sorted_int[i].end <= sorted_int[i+1].start:
                print("here")
                continue
            return False
        
        return True

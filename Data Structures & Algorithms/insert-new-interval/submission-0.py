class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0
        n = len(intervals)
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # insert, merge if needed
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        res.append(newInterval)

        while i < n and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1

        return res
        

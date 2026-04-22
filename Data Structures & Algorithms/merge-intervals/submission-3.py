class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        n = len(intervals)
        i = 1
        res = [intervals[0]]

        while i < n:
            print(res, i)
            if intervals[i][0] <= res[-1][1]:
                res[-1] = [min(intervals[i][0], res[-1][0]), max(intervals[i][1], res[-1][1])]            
            else:
                res.append(intervals[i])
            i += 1

        return res




class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        i = 0
        n = len(intervals)
        res = []

        while i < n:

            if i > 0:
                if intervals[i][0] <= res[-1][1]:
                    res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
                else:
                    res.append(intervals[i])

            else:
                res.append(intervals[i])

            i += 1

        return res


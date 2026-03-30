import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        idx = bisect.bisect_right([row[0] for row in matrix], target)
        print(idx)
        if idx == 0:
            return False

        for val in matrix[idx-1]:
            if val == target:
                return True

        return False

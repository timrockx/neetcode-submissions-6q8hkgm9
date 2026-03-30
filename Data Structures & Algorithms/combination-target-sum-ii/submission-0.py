class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        curr = []

        def dfs(i, curr_sum):

            if curr_sum == target:
                res.append(curr.copy())
                return

            for j in range(i, len(candidates)):
                if curr_sum > target:
                    break

                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                curr.append(candidates[j])
                curr_sum += candidates[j]
                # deeper on next element
                dfs(j+1, curr_sum)
                curr.pop()
                curr_sum -= candidates[j]

        dfs(0, 0)
        return res
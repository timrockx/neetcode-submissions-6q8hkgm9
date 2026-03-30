class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []
        available = set(nums)

        def dfs():

            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in list(available):

                curr.append(num)
                available.remove(num)
                dfs()

                curr.pop()
                available.add(num)
        
        dfs()
        return res

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_map = defaultdict(list)
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)
        visited = set()
        
        def dfs(i):
            if i in visited:
                return False
            
            visited.add(i)
            for prereq in pre_map[i]:
                if not dfs(prereq):
                    return False
            visited.remove(i)
            pre_map[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            


        

        
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_map = defaultdict(list)
        for course, prereq in prerequisites:
            pre_map[prereq].append(course)
        visited = set()
        print(pre_map)
        
        def dfs(i):
            
            if i == numCourses and len(visited) == numCourses:
                return True
            
            if i in visited:
                return False
            
            visited.add(i)
            for course in pre_map[i]:
                if not dfs(course):
                    return False
            visited.remove(i)
            pre_map[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            


        

        
        
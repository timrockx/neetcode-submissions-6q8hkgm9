class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre_map = defaultdict(list)
        inorder = [0] * numCourses
        res = []

        for course, prereq in prerequisites:
            pre_map[prereq].append(course)
            inorder[course] += 1
        
        q = deque()

        for i in range(numCourses):
            if inorder[i] == 0:
                q.append(i)
            
        while q:
            course = q.popleft()
            res.append(course)
            for crs in pre_map[course]:
                inorder[crs] -= 1
                if inorder[crs] == 0:
                    q.append(crs)

        return res if len(res) == numCourses else []
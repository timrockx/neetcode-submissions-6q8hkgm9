class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_map = defaultdict(list)
        indegree = [0] * numCourses
        res = []

        for course, prereq in prerequisites:
            pre_map[prereq].append(course)
            indegree[course] += 1

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            res.append(course)
            for dep in pre_map[course]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    q.append(dep)

        return len(res) == numCourses
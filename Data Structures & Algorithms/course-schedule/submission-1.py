class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        unlocks = [[] for i in range(numCourses)]
        prereq = [0] * numCourses
        for course, prerequisite in prerequisites:
            unlocks[prerequisite].append(course)
            prereq[course] += 1
        queue = deque(
            course for course in range(numCourses) if prereq[course] == 0
        )
        completed = 0 
        while queue:
            course = queue.popleft()
            completed += 1
            for next_course in unlocks[course]:
                prereq[next_course] -= 1
                if prereq[next_course] == 0:
                    queue.append(next_course)
        return completed == numCourses
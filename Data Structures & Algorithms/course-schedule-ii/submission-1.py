from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unlocks = [[] for i in range(numCourses)]
        prereq = [0] * numCourses

        for course, prerequisite in prerequisites:
            unlocks[prerequisite].append(course)
            prereq[course] += 1
        
        queue = deque(
            course for course in range(numCourses) if prereq[course] == 0
        )

        completed = []
        while queue:
            course = queue.popleft()
            completed.append(course)
            for next_course in unlocks[course]:
                prereq[next_course] -= 1
                if prereq[next_course] == 0:
                    queue.append(next_course)
        return completed if len(completed) == numCourses else []
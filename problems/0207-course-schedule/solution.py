from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        dependents = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for course, prerequisite in prerequisites:
            dependents[prerequisite].append(course)
            indegrees[course] += 1
        ready = deque(course for course, degree in enumerate(indegrees) if degree == 0)
        completed = 0
        while ready:
            course = ready.popleft()
            completed += 1
            for dependent in dependents[course]:
                indegrees[dependent] -= 1
                if indegrees[dependent] == 0:
                    ready.append(dependent)
        return completed == numCourses

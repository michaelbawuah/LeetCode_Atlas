from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        dependents = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for course, prerequisite in prerequisites:
            dependents[prerequisite].append(course)
            indegrees[course] += 1
        ready = deque(course for course, degree in enumerate(indegrees) if degree == 0)
        ordering = []
        while ready:
            course = ready.popleft()
            ordering.append(course)
            for dependent in dependents[course]:
                indegrees[dependent] -= 1
                if indegrees[dependent] == 0:
                    ready.append(dependent)
        return ordering if len(ordering) == numCourses else []

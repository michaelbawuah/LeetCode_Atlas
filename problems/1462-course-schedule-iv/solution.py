class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        reach = [[False] * numCourses for _ in range(numCourses)]
        for before, after in prerequisites:
            reach[before][after] = True
        for via in range(numCourses):
            for first in range(numCourses):
                if reach[first][via]:
                    for last in range(numCourses):
                        reach[first][last] |= reach[via][last]
        return [reach[first][last] for first, last in queries]

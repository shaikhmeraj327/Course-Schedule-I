from collections import deque


def can_finish(num_courses, prerequisites):
    adjacency = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, prerequisite in prerequisites:
        adjacency[prerequisite].append(course)
        in_degree[course] += 1

    queue = deque(course for course in range(num_courses) if in_degree[course] == 0)
    completed = 0

    while queue:
        current = queue.popleft()
        completed += 1
        for dependent in adjacency[current]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    return completed == num_courses


def canFinish(numCourses, prerequisites):
    return can_finish(numCourses, prerequisites)


class Solution:
    def canFinish(self, numCourses, prerequisites):
        return can_finish(numCourses, prerequisites)

    def isPossible(self, n, prerequisites):
        return can_finish(n, prerequisites)

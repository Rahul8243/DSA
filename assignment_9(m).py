# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
#  You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
#  that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = set()      # Courses fully processed
        path = set()         # Current recursion path

        def dfs(course):
            # Cycle detected
            if course in path:
                return False
            # Already processed → no issue
            if course in visited:
                return True

            path.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            path.remove(course)
            visited.add(course)

            return True

        # Check all courses (in case the graph is disconnected)
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.


from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"  # mark as visited

            while queue:
                x, y = queue.popleft()

                # Explore all 4 directions
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    # Check boundaries and if it's land
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"  # mark visited
                        queue.append((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)

        return count

# #Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            print("Grid is empty!")
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"  # mark as visited
            print(f"  Starting BFS from ({r}, {c})")

            while queue:
                x, y = queue.popleft()
                print(f"    Visiting ({x}, {y})")

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        print(f"      Found connected land at ({nx}, {ny}) → marking visited")
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))

        print("Initial Grid:")
        for row in grid:
            print(" ".join(row))
        print()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    print(f"\nIsland #{count} found at ({r}, {c})")
                    bfs(r, c)

        print(f"\nTotal islands found: {count}")
        return count
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Solution().numIslands(grid)

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
# The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] 
# represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly
#  north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
#  Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes tha
# t rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

#-----------------------------------------------------------------------
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            # Out of bounds or smaller height → stop
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or heights[r][c] < prev_height):
                return
            
            visited.add((r, c))
            # Explore neighbors
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Start DFS from Pacific and Atlantic borders
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])         # Pacific (top row)
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Atlantic (bottom row)
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])         # Pacific (left column)
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Atlantic (right column)

        # Intersection of reachable cells
        result = list(pacific & atlantic)
        return result

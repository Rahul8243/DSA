# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # If all characters in word are matched
            if i == len(word):
                return True
            
            # Check boundaries and character match
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]):
                return False

            # Temporarily mark the current cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all four directions
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            # Restore the cell (backtrack)
            board[r][c] = temp

            return found

        # Try to start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

#Given the root of a binary tree, 
# return the bottom-up level order traversal of its nodes' values.
#  (i.e., from left to right, level by level from leaf to root).

from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        
        # Reverse to get bottom-up order
        return result[::-1]


# 🔹 Example Usage (print section)
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Call the solution
    sol = Solution()
    output = sol.levelOrderBottom(root)
    
    # Print the result
    print("Bottom-up Level Order Traversal:")
    print(output)

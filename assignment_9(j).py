# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        def dfs(node, level):
            if not node:
                return
            
            # If we reach a new level, add a new list
            if len(levels) == level:
                levels.append([])
            
            # Add the current node's value to its level list
            levels[level].append(node.val)
            
            # Recurse left and right, increasing level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return levels

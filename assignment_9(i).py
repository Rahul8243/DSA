# Given the root of a binary tree and an integer targetSum, return true if the tree has a 
# root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if tree is empty
        if not root:
            return False
        
        # If it's a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check left or right subtree with updated sum
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))


# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Definition for a binary tree node.

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Helper function to compare two nodes
        def isMirror(t1, t2):
            # If both nodes are None → symmetric
            if not t1 and not t2:
                return True
            # If only one is None → not symmetric
            if not t1 or not t2:
                return False
            # Both values must be equal, and their children must be mirrors
            return (t1.val == t2.val) and \
                   isMirror(t1.left, t2.right) and \
                   isMirror(t1.right, t2.left)

        # Start the recursion comparing left and right subtree
        return isMirror(root.left, root.right)

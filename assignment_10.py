# Given a root node reference of a BST and a key, delete 
# the node with the given key in the BST. Return the root 
# node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # Base case: empty tree
        if not root:
            return None
        
        # Step 1: Search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Step 2: Node found — handle deletion cases

            # Case 1: No left child
            if not root.left:
                return root.right
            
            # Case 2: No right child
            elif not root.right:
                return root.left
            
            # Case 3: Two children
            # Find inorder successor (smallest value in right subtree)
            min_node = self.findMin(root.right)
            
            # Copy the successor's value to this node
            root.val = min_node.val
            
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root

    # Helper function to find the smallest node in a subtree
    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

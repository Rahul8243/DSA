#Question 3: Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        # Base case
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        # Recursively build left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root


# ---------- PRINT SECTION ----------
from collections import deque

# Inorder Traversal (should match sorted array)
def inorderTraversal(root):
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

# Level Order Traversal (to visualize structure)
def levelOrderTraversal(root):
    if not root:
        return []
    result, queue = [], deque([root])
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
    return result


# ---------- MAIN DRIVER ----------
if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted array elements (space-separated): ").split()))
    
    sol = Solution()
    root = sol.sortedArrayToBST(nums)
    
    print("\n Inorder Traversal of BST:")
    print(inorderTraversal(root))
    
    print("\n Level Order Traversal (structure view):")
    for level in levelOrderTraversal(root):
        print(level)

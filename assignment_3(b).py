# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node

        return helper(0, len(nums) - 1)

# ---------------- Helper function to print the BST ----------------
def printLevelOrder(root):
    if not root:
        return
    from collections import deque
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            print(node.val, end=" ")
            q.append(node.left)
            q.append(node.right)
    print()

# ---------------- Usage ----------------
nums = [-10, -3, 0, 5, 9]
root = Solution().sortedArrayToBST(nums)
print("Level-order traversal of BST:")
printLevelOrder(root)

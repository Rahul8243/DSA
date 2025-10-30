#You are given the root of a Binary Tree consisting of NN nodes, rooted at node 11.
# Your task is to return the Inorder Traversal of the given tree.
# Input:
# •	First line will contain TT, number of test cases. Then the test cases follow.
# •	Each test case contains single lines of input.
# •	The first line contains the Binary Tree representation in the order of level order
#  Traversal where, numbers denote node values, and a character NN denotes NULL child.


from collections import deque

# Definition for a binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to build tree from level order input
def buildTree(level_order):
    if not level_order or level_order[0] == 'N':
        return None
    
    root = Node(int(level_order[0]))
    queue = deque([root])
    i = 1
    
    while queue and i < len(level_order):
        current = queue.popleft()
        
        # Left child
        if level_order[i] != 'N':
            current.left = Node(int(level_order[i]))
            queue.append(current.left)
        i += 1
        
        if i >= len(level_order):
            break
        
        # Right child
        if level_order[i] != 'N':
            current.right = Node(int(level_order[i]))
            queue.append(current.right)
        i += 1
    
    return root

# Inorder traversal (recursive)
def inorderTraversal(root, result):
    if root:
        inorderTraversal(root.left, result)
        result.append(root.data)
        inorderTraversal(root.right, result)


if __name__ == "__main__":
    T = int(input("Enter number of test cases: ").strip())
    
    for t in range(T):
        print(f"\nTest case {t+1}:")
        level_order = input("Enter level order traversal (use N for null): ").strip().split()
        
        root = buildTree(level_order)
        
        result = []
        inorderTraversal(root, result)
        
        # Printing the result
        print("Inorder Traversal Output:")
        print(*result)

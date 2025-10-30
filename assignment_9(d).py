# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            print("Graph is empty!")
            return None

        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val)
        print(f"Cloned starting node: {node.val}")

        while queue:
            current = queue.popleft()
            print(f"\nVisiting node: {current.val}")

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    # Clone neighbor
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                    print(f"  Cloned neighbor node: {neighbor.val}")

                # Connect current clone to neighbor clone
                visited[current].neighbors.append(visited[neighbor])
                print(f"  Added edge: {current.val} → {neighbor.val}")

        print("\n Cloning complete!")
        return visited[node]
# Build sample graph:
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]


cloned = Solution().cloneGraph(node1)


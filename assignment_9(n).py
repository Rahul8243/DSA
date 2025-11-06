# You are given a network of n nodes, labeled from 1 to n. You are also given times,
#  a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, 
# vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes
#  to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Min-heap: (time, node)
        min_heap = [(0, k)]
        dist = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            # Skip if already visited
            if node in dist:
                continue
            dist[node] = time
            # Explore neighbors
            for nei, wt in graph[node]:
                if nei not in dist:
                    heapq.heappush(min_heap, (time + wt, nei))
        
        # If all nodes received the signal
        if len(dist) == n:
            return max(dist.values())
        return -1

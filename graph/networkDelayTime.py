from collections import defaultdict
from heapq import *
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, cost in times: 
            adj[src].append((dst, cost))
        pq = [(0, k)]
        visited = set()
        result = 0
        while pq: 
            time, node = heappop(pq)
            if node in visited:
                continue 
            result = time 
            visited.add(node)
            for nei, cost in adj[node]: 
                heappush(pq, (time+cost, nei))
        if len(visited) == n: 
            return result 
        return -1 

# Time: O(ElogN)
# Space: O(E+N)
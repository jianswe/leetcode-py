from collections import defaultdict
from typing import List 

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        adj = defaultdict(set)
        count = 0
        for room1, room2 in corridors: 
            adj[room1].add(room2)
            adj[room2].add(room1)
            count += len(adj[room1].intersection(adj[room2])) 
        return count 
    
# Time: O(E*N), Space: O(N^2)
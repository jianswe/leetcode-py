from typing import List 

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.grid = grid 
        self.N = len(grid)
        if grid[0][0] == 1: 
            return -1 
        queue = [(0,0)]
        visited = set((0,0))
        ans = 1
        while(queue): 
            next_queue = []
            for node in queue: 
                r,c = node 
                if r==self.N-1 and c==self.N-1: 
                    return ans 
                for nei in self.neighbors(r,c): 
                    nr, nc = nei 
                    if self.valid(nr,nc) and grid[nr][nc]==0 and nei not in visited: 
                        next_queue.append(nei)
                        visited.add(nei)
            ans+=1
            queue = next_queue
        return -1 

    def neighbors(self, i, j): 
        return [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]
    
    def valid(self, i, j):
        return 0<=i and i<self.N and 0<=j and j<self.N
    
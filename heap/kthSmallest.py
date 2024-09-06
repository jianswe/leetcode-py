from typing import List
from heapq import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapify(min_heap)
        for _ in range(k):
            smallest, i, j = heappop(min_heap)
            if j+1<n:
                heappush(min_heap, (matrix[i][j+1], i, j+1))
        return smallest
from typing import List
from heapq import *

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        neg_piles = [-pile for pile in piles]
        heapify(neg_piles)
        for i in range(k):
            pile = -heappop(neg_piles)
            remain = pile - pile//2
            heappush(neg_piles, -remain)
        return -sum(neg_piles)

# time: O(N + klogN)
# space: O(N)
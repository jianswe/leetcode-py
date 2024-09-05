from typing import List
from heapq import *

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capfits = list(zip(capital, profits))
        heapify(capfits)
        neg_profits = []
        heapify(neg_profits)
        for i in range(k):
            while capfits and capfits[0][0]<=w:
                cap, fit = heappop(capfits)
                heappush(neg_profits, -fit)
            if neg_profits: 
                max_fit = -heappop(neg_profits) 
                w += max_fit
        return w 
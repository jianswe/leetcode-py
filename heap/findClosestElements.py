from typing import List
from heapq import *

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        k_closest_max_heap = []
        for num in arr: 
            heappush(k_closest_max_heap, (-abs(num - x), -num))
            if len(k_closest_max_heap) > k: 
                heappop(k_closest_max_heap)
        return sorted([-neg_num for neg_dis, neg_num in k_closest_max_heap])
from collections import Counter
from heapq import *
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        topK_min_heap = []
        for num, count in freq.items():
            heappush(topK_min_heap, (count, num)) 
            if len(topK_min_heap) > k:
                heappop(topK_min_heap) 
        return [num for count, num in topK_min_heap]
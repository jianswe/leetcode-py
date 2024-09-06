from heapq import *

class MedianFinder:

    def __init__(self):
        self.max_heap_for_smallnum = []
        self.min_heap_for_largenum = []

    def addNum(self, num: int) -> None:
        if not self.max_heap_for_smallnum:
            self.max_heap_for_smallnum = [-num]
            return 
        median = self.findMedian()
        if num <= median:
            heappush(self.max_heap_for_smallnum, -num)
            if len(self.max_heap_for_smallnum) > len(self.min_heap_for_largenum)+1: 
                temp = -heappop(self.max_heap_for_smallnum)
                heappush(self.min_heap_for_largenum, temp)
        else: 
            heappush(self.min_heap_for_largenum, num)
            if len(self.min_heap_for_largenum) > len(self.max_heap_for_smallnum):
                temp = heappop(self.min_heap_for_largenum)
                heappush(self.max_heap_for_smallnum, -temp)

    def findMedian(self) -> float:
        if len(self.max_heap_for_smallnum) == len(self.min_heap_for_largenum):
            return (self.min_heap_for_largenum[0] - self.max_heap_for_smallnum[0])/2
        return -self.max_heap_for_smallnum[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
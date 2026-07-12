import heapq
class MedianFinder:

    def __init__(self):
        #initialize the small -> maxheap , large -> minheap
        self.small , self.large = [],[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1 * num)

        #INVARIANT 1 -> elements in small <= large
        if (self.small and self.large 
                and (-1 *self.small[0] > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        #INVARIANT 2 -> dealing with uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1 * val)

    def findMedian(self) -> float:
        # ODD length small heap has more elements
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
         # ODD length large heap has more elements
        elif len(self.large) > len(self.small):
            return self.large[0]
        # EVEN length
        else:
            return (-1 * self.small[0] + self.large[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
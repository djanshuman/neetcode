class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # INITIALIZATION
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist,x,y))
        
        #heapify to give it a heap structure 
        heapq.heapify(minHeap)

        # Pop k times to get values and return res
        res = []
        while k > 0:
            (dist, x, y) = heapq.heappop(minHeap)
            res.append([x,y])
            k -=1
        return res
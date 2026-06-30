from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_map = {}
        min_heap = []

        for i in nums:
            heap_map[i] = heap_map.get(i,0) + 1

        for key,val in heap_map.items():
            heappush(min_heap, (val,key))
            if len(min_heap) > k:
                heappop(min_heap)

        return [key for val ,key in min_heap]
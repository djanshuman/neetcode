import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)

            if first > second:
                heapq.heappush(stones, -1 * (first - second))
            elif second > first:
                heapq.heappush(stones, -1 * (second - first))
        
        stones.append(0)
        return (-1 * stones[0])
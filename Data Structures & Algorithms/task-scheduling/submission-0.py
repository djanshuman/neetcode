import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #each task takes n unit of time
        # minimize idle time
        count = {}
        time = 0
        q = deque() # [-cnt, t]
        for i in tasks:
            count[i] = count.get(i,0) + 1
        maxHeap = [- val for key, val in count.items()]
        heapq.heapify(maxHeap)
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                if val:
                    q.append([val,time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time



#bucket sort solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        bucket = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            freq_map[i] = freq_map.get(i,0) + 1
        
        for key, val in freq_map.items():
            bucket[val].append(key)
        
        res = []
        for i in range(len(bucket) - 1 , 0 , -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

'''
# O(nlogk) solution
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = dict()
        myheap = []
        
        for i in nums:
            mydict[i] = mydict.get(i,0) + 1

        for key,val in mydict.items():
            heapq.heappush(myheap,(val,key))
            if len(myheap) > k:
                heapq.heappop(myheap) # evict least frequent

        return [key for val, key in myheap]

'''
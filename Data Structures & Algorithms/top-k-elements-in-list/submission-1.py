class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = dict()

        for i in nums:
            mydict[i] = mydict.get(i,0) + 1
        
        # Use frequency bucket approach
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, val in mydict.items():
            buckets[val].append(key)
        #[[], [3], [2], [1], [], [], []]

        res = []
        for i in range(len(buckets) -1, -1,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele_map = {}
        # bucket sort, create empty buckets based on len of input array
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            ele_map[n] = 1 + ele_map.get(n, 0)

        for n, c in ele_map.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                if len(res) != k:
                    res.append(j)
        return res
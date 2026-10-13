class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0]
        for wt in w:
            self.prefix.append(self.prefix[-1] + wt)

    def pickIndex(self) -> int:
        target = self.prefix[-1] * random.random()
        l = 0
        r = len(self.prefix) -1
        pos = -1
        while l <= r:
            mid =(l + r) // 2
            if self.prefix[mid] > target:
                pos = mid
                r = mid - 1
            else:
                l = mid + 1

        return pos - 1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
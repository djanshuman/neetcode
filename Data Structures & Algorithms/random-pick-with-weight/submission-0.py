class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)

    def pickIndex(self) -> int:
        target_sum = self.total * random.random()
        cumm_sum = 0
        for i in range(len(self.w)):
            cumm_sum += self.w[i]
            if cumm_sum > target_sum:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class Solution:
    
    def feasible_solution(self,piles,k,h):
        num_hours = 0
        for i in piles:
            num_hours += math.ceil(i/k)
        return num_hours <= h
    
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = -1

        while l <= r :
            mid = (l + r) // 2
            if self.feasible_solution(piles ,mid, h):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
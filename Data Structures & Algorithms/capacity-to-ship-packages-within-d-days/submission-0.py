class Solution:
    def feasible_solution(self, weights, capacity, days):
        no_of_days = 1             # always at least 1 day
        total = 0
        for w in weights:
            if total + w <= capacity:
                total += w
            else:
                total = w          # start new day
                no_of_days += 1
        return no_of_days <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)           # min capacity = heaviest package
        r = sum(weights)           # max capacity = ship everything in 1 day
        ans = -1

        while l <= r:
            mid = (l + r) // 2
            if self.feasible_solution(weights, mid, days):
                ans = mid
                r = mid - 1        # try smaller capacity
            else:
                l = mid + 1        # capacity too small

        return ans                 # ← not mid
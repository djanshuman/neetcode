class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Bottom up approach with Space optimization
        n = len(nums)
        tot_sum = 0
        for i in range(n):
            tot_sum += nums[i]
        if tot_sum % 2 != 0:
            return False
        target = tot_sum //2

        prev = [False] * (target + 1)
        prev[0] = True

        if nums[0] <= target:
            prev[nums[0]] = True

        for i in range(1, n):
            curr = [False] * (target + 1)
            curr[0] = True
            for j in range(1, target + 1):
                not_take = prev[j]
                take = False
                if j >= nums[i]:
                    take = prev[j - nums[i]]
                curr[j] = take or not_take
            prev = curr
        return prev[target]

  


   
'''
Top down with Memo
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        


        def calc_sub_sum(idx, target):

            if target == 0:
                return True

            if idx == 0:
                return nums[idx] == target

            if dp[idx][target] != -1:
                return dp[idx][target]

            not_take = calc_sub_sum(idx - 1, target)
            take = False
            if target >= nums[idx]:
                take = calc_sub_sum(idx - 1, target - nums[idx])
            
            dp[idx][target] = take or not_take
            return dp[idx][target]

        n = len(nums)
        sum = 0
        for i in range(n):
            sum += nums[i]
        if sum % 2 != 0:
            return False
        target = sum //2
        dp = [[-1] * (target + 1) for _ in range(n)]
        return calc_sub_sum(n - 1, target)
'''
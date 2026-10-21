class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #[-4,-1,-1,0,1,2,]

        for i, a in enumerate(nums):
            # ensure next element should be same as before a should be unique
            if i > 0 and nums[i] == nums[i - 1]:
                continue


            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -=1

                elif three_sum < 0:
                    l += 1

                else:
                    res.append([a,nums[l], nums[r]])
                    l += 1

                    #ensure next element of l isn't the same else it may duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
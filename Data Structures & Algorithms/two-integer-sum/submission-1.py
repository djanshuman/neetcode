class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myset = {}

        for i ,n in enumerate(nums):
            diff = target - n
            if diff in myset:
                return [myset[diff],i]
            myset[n] = i
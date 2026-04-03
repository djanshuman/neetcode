class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        maxLength = 0

        for n in myset:
            length = 0
            if (n - 1) not in myset:
                while (n + length) in myset:
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength
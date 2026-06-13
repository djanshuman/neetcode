class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def backtrack(idx):
            res.append(path[:])

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()


        backtrack(0)
        return res
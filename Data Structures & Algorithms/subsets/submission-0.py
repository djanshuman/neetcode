class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path =[]

        def backtrack(idx):
            if idx >= len(nums):
                res.append(path[:])
                return

            # include element 
            path.append(nums[idx])
            backtrack(idx + 1)

            # do not include element
            path.pop()
            backtrack(idx + 1)

        backtrack(0)
        return res
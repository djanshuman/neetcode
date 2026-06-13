class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(idx, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(idx, len(candidates)):
                # Skip duplicates
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                # Early break-in as sorted and remaining elements will never arrive at target
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                # i + 1 is passed instead of i as compared to I problem as reuse is not allowed. 
                backtrack(i + 1, remaining - candidates[i])
                path.pop()

        backtrack(0,target)
        return res

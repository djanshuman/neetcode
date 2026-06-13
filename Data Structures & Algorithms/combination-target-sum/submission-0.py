class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # STEP 1: INITIALIZATION
        
        res = []
        path = []

        # Sort so candidates are ascending -> enables the early `break` prune below.
        # (Candidates are distinct here, so this is NOT about grouping duplicates.)
        candidates.sort()

        def backtrack(idx, remaining):
            
            #BASE CASE , IF WE HAVE REACHED THE COMBINATION FOR TARGET
            if remaining == 0:
                res.append(path[:])
                return
            

            for i in range(idx , len(candidates)):
                # Early break-in , SINCE SORTED, SO ALL REMAINING WILL NEVER REACH TARGET
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                path.pop()


        backtrack(0,target)
        return res
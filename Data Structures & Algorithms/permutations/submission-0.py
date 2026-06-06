class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        used = [False] * len(nums)

        def generateLetters(start_idx):
            if start_idx == len(nums):
                res.append(path[:])
                return 

            
            for idx, element in enumerate(nums):
                if used[idx]:
                    continue
                path.append(element)
                used[idx] = True
                generateLetters(start_idx + 1)
                path.pop()
                used[idx] = False

        generateLetters(0)
        return res
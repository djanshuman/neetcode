class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def generateSubStringPartition(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                sub = s[start : end]
                if sub == sub[:: -1]: # palindrome check
                    path.append(sub)
                    generateSubStringPartition(end, path)
                    path.pop()        # backtrack

        res = []
        generateSubStringPartition(0, [])
        return res

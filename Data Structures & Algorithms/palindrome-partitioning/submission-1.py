class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        


        def partitionSubstring(start, path):
            if start == len(s):
                res.append(path[:])
                return


            for end in range(start + 1 , len(s) + 1):
                sub = s[start : end]
                if sub == sub[:: -1]:
                    path.append(sub)
                    partitionSubstring(end, path)
                    path.pop()

        partitionSubstring(0, [])
        return res
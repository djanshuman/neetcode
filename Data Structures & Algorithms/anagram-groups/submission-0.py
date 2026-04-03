from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list)

        for c in strs:
            count =[0]*26
            for j in c:
                count[ord(j)- ord('a')] +=1
            
            res[tuple(count)].append(c)
        return list(res.values())
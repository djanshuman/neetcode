class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS={}
        countT={}

        for c in range(len(s)):
            countS[s[c]] = 1 + countS.get(s[c],0)
            countT[t[c]] = 1 + countT.get(t[c],0)

        for e in countS:
            if countS[e] != countT.get(e,0):
                return False
        return True
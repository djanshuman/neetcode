class Solution:
    def countSubstrings(self, s: str) -> int:
        reslen = 0

        def expand(l,r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -=1
                r += 1
            return count

        
        for i in range(len(s)):
            reslen += expand(i,i)
            reslen += expand(i,i + 1)
        return reslen



'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0

        for i in range(len(s)):
            l,r=i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1

            l,r=i,i+1
            while l >=0 and r < len(s) and s[l] == s[r]:

                count += 1
                l-=1
                r+=1
        return count
'''
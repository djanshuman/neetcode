class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand(l, r):
            
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1: r]

        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i + 1)

            for ele in (odd,even):
                if len(ele) > len(res):
                    res = ele
        return res



'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0

        for i in range(len(s)):
            # odd length
            l,r=i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r -l +1) > resLen:
                    res=s[l:r+1]
                    resLen= (r-l+1)
                l-=1
                r+=1
            # even length
            l,r= i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if( r- l +1) > resLen:
                    res= s[l:r+1]
                    resLen= (r-l+1)
                l-=1
                r+=1
        return res

'''
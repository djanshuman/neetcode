class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r  = 0 , len(s) - 1

        def palin_check(i , j):

            while i < j :
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True


        while l < r :
            
            if s[l] != s[r]:
                return palin_check(l +1 ,r) or palin_check(l , r - 1)
            l += 1
            r -= 1
            
        return True
        
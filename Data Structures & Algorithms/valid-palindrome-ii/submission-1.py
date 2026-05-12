class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s) - 1

        #1. This block receives an incremented indices from the last palindrome failed check index.
        #2. On 1st mismatch occurs, this function is invoked which checks all futher string must be palindrome.
        def isPalin(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        #3. This checks the palindrome and calls for helper method when 1st mismatch is found to validate left over String.
        #4. If no mismatch found then proceed for usual palindrome check
        while l < r:
            if s[l] != s[r]:
                return isPalin(l+1 ,r) or isPalin(l ,r-1)
            l += 1
            r -= 1
        return True

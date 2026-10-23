class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        l = 0
        mydict = dict()
        maxf = 0 #tracking highest frequency seen so far

        for r in range(len(s)):
            ele = s[r]
            mydict[ele] = mydict.get(ele,0) + 1

            # Every innsert we are checking if we beat the maxf we have seen so far.
            # Even if l shrinks and freq go down but at one point it was true and untill new highest frequency shows up, thats still true
            maxf = max(maxf, mydict[ele])

            # Keeping window valid 
            while (r - l + 1) - maxf > k:
                left = s[l]
                mydict[left] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)

        return maxlen

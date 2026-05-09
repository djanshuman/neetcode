class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # STEP 1 : Initialize variables
        
        if t == "" : return ""

        countS = dict()
        countT = dict()

        for i in t:
            countT[i] = countT.get(i,0) + 1

        have , need = 0 , len(countT)
        l = 0
        res, resLen = [-1,-1] , float("infinity")

        # STEP 2 : Iterate through the String S and find minimum window and shrink left and update length
        for r in range(len(s)):
            ele = s[r]
            countS[ele] = countS.get(ele, 0) + 1

            # STEP 3: If the element is part of our need and count matches then increment have by 1
            if ele in countT and countT[ele] == countS[ele]:
                have += 1
            
            # STEP 4 : while the invariant is true and valid window, can we find smaller window
            while have == need:
                
                # STEP 5 : update window length, capture state
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l ,r]

                left = s[l]
                countS[left] -= 1
                if left in countT and countS[left] < countT[left]:
                    have -= 1

                l += 1

        l , r = res
        return s[l : r + 1] if resLen != float('infinity') else ""

    


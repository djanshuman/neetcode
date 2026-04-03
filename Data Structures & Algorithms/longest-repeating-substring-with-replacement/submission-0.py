class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        resLen = 0
        counterS = {}
        l = 0

        for r in range(len(s)):
            counterS[s[r]] = 1 + counterS.get(s[r], 0)

            while (r - l + 1) - max(counterS.values()) > k:
                counterS[s[l]] -= 1
                l += 1
            resLen = max(resLen, r - l + 1)

        return resLen
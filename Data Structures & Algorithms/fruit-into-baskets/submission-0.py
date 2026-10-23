class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        maxWindowlen = 0
        freq = dict()
        l = 0
        
        for r in range(len(fruits)):
            freq[fruits[r]] = freq.get(fruits[r],0) + 1

            if len(freq) > 2:
                left = fruits[l]
                freq[left] -=1
                if freq[left] == 0:
                    del freq[left]
                l +=1

            maxWindowlen = max(maxWindowlen, r - l + 1)
        return maxWindowlen
            
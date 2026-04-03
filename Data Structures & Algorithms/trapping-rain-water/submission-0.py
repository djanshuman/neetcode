class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        sum = 0

        while l < r:
            if lmax < rmax:
                l +=1 
                lmax = max(lmax, height[l])
                sum += lmax - height[l]

            else:
                r -= 1
                rmax = max(rmax, height[r])
                sum +=  rmax - height[r]
        return sum

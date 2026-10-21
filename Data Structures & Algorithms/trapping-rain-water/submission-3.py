# using two pointer solution
# no extra space O(1)
# shortest height is always bottleneck 
# track max of l and r as we traverse
# since min height is bottle neck so for each index min(l,r) - height[i]
# O(n) time
class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 0:
            return 0

        maxL = float('-inf')
        maxR = float('-inf')

        l = 0
        r = len(height) - 1
        area = 0

        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            if height[l] < height[r]:
                area += min(maxL,maxR) - height[l]
                l += 1

            elif height[r] < height[l]:
                area += min(maxL,maxR) - height[r]
                r -= 1

            else:
                l +=1

        return area


'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # Step -1 Initialize variables
        l , r = 0 , len(height) - 1
        maxL, maxR = height[l] , height[r]
        res = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL,height[l])
                res += maxL - height[l]
            else:
                r -=1
                maxR = max(maxR,height[r])
                res += maxR - height[r]
        return res
'''
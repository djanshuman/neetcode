class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
                
            # If the left portion is sorted
            if nums[l] <= nums[mid]:
                # Target is in the right side if it's larger than mid 
                # OR smaller than the smallest value in the left portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # Otherwise, the right portion must be sorted
            else:
                # Target is in the left side if it's smaller than mid
                # OR larger than the largest value in the right portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return -1
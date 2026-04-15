class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        
        # 1. Find the index of the smallest element (Pivot)
        l = 0
        r = len(nums) - 1
        pivot = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= nums[-1]:
                pivot = mid
                r = mid - 1
            else:
                l = mid + 1

        # 2. Select the correct sorted half
        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot - 1

        # 3. Standard Binary Search on the selected half
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1
        return -1
    




            
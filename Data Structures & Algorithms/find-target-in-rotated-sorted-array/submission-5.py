class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0

        if nums[-1] == target:
            return len(nums) - 1

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

        if nums[pivot] == target:
            return pivot

        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            l = pivot
            r = len(nums) - 1

        else:
            l = 0
            r = pivot - 1

        idx = -1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1
        return idx
    




            
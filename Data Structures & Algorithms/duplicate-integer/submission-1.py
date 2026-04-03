class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for ele in nums:
            if ele in hashSet:
                return True
            hashSet.add(ele)
        return False
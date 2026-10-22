class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = dict()
        curr_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            # 1. add the element to dict and update sum
            curr_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i],0) + 1

            # 2. Out of window , slide and update state and sum
            # this will be execute only after k - 1 initial elements from index 3 
            if i >= k:
                curr_sum -= nums[ i - k]
                freq[nums[i - k]] -=1
                if freq[nums[i - k ]] == 0:
                    del freq[nums[i-k]]

            #record max sum whenenver window is 3
            if i >= k - 1:
                if len(freq) == k:
                    max_sum = max(max_sum,curr_sum)

        return max_sum if max_sum != float('-inf') else 0



'''
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        counter = dict()
        maxsum = float('-inf')
        for i in range(len(nums)):
            # 1. Add the right element
            currSum += nums[i]
            counter[nums[i]] = counter.get(nums[i],0) + 1
            # 2. If window size gets out of K , shrink from left
            if i >= k:
                currSum -= nums[i-k]
                counter[nums[i - k]] -= 1
                if counter[nums[i - k]] == 0:
                    del counter[nums[i - k]]
            # 3. Check unique elements count in dictionary and record maxSum
            if i >= k - 1:
                if len(counter) == k:
                    maxsum = max(maxsum,currSum)

        return maxsum  if maxsum != float('-inf') else 0
        

                
'''
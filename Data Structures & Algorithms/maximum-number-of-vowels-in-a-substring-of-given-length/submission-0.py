class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_val = 0
        my_set = {'a','e','i','o','u'}
        curr_vowel_count = 0

        #bootstrap initial window
        for i in range(k):
            if s[i] in my_set:
                curr_vowel_count += 1

        #update counter
        max_val = max(max_val, curr_vowel_count)

        for i in range(k,len(s)):
            left = s[i - k]
            right = s[i]
            
            #a. if leaving char was a vowel, decrement it
            if left in my_set:
                curr_vowel_count -=1
            
            #b. if adding char is a vowel, update state
            if right in my_set:
                curr_vowel_count += 1
            
            #c. update max vowel seen
            max_val = max(max_val, curr_vowel_count)

        return max_val


'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr_length = 0
        vowel_set = {'a','e','i','o','u'}
        curr_length = sum(1 for c in s[:k] if c in vowel_set )
        max_length = curr_length
        
        # Traverse and remove left and add right
        for i in range(k, len(s)):
            if s[i -k] in vowel_set:
                curr_length -= 1
            if s[i] in vowel_set:
                curr_length += 1
            max_length = max(max_length,curr_length )
        return max_length
                

'''
class Solution:
    def isHappy(self, n: int) -> bool:
        # Calculate sum of squares of digit of a number
        def get_sum_of_squares(n):
            total = 0
            while n > 0:
                digit = n % 10
                digit = digit ** 2
                total += digit
                n //= 10
            return total
        # Assign slow and fast , keep fast ahead of slow , so that in while, it doesn't terminate in first line.
        slow = n
        fast = get_sum_of_squares(n)
        # If unhappy then fast keep hitting same number then slow and fast will eventually meet some point and loop will terminate
        # If happy then fast will hit 1 and loop will terminate
        while fast != 1 and slow != fast:
            slow = get_sum_of_squares(slow)
            fast = get_sum_of_squares(get_sum_of_squares(fast))
        return fast == 1


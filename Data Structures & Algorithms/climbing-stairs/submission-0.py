class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

'''
class Solution:
    # bottom-up/iterative
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        first , second = 1 , 2
        for i in range(3,n + 1):
            third = first + second
            first,second = second, third
        return third

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''Rules'''
        #1. Add Open till open < n
        #2. Closed to be added if closedN < openN
        #3. Base case: Valid result if openN == closedN == n


        # Initialize member variables
        res = []
        stack =[]


        def backtracking(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtracking(openN, closedN + 1)
                stack.pop()

        backtracking(0, 0)
        return res

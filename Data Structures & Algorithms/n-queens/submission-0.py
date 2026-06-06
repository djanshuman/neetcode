class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        def isValid(x, k , l):

            for i in range(1 , k):
                if (x[i] == l) or abs(i - k) == abs(x[i] - l):
                    return False
            return True 

        def generateQueens(x ,k, n, res):
            for i in range(1 , n + 1):
                if isValid(x, k , i):
                    x[k] = i
                    if k == n:
                        board = []
                        for row in range(1, n+1):
                            line = "." * (x[row] - 1) + "Q" + (n - x[row]) * "."
                            board.append(line)
                        res.append(board)
                    
                    else:
                        generateQueens(x ,k + 1, n, res)
        x = [0] * (n + 1)
        res =[]
        generateQueens(x ,1, n, res)
        return res
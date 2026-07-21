
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up with memo and dp
        ROWS, COLS = m , n
        dp = [[-1] * (COLS) for _ in range(ROWS)] # [[-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1]]
     
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 and col == 0:
                    dp[0][0] = 1
                    continue
                up = 0
                down = 0  
                if row > 0:
                    up = dp[row - 1][col]
                if col > 0:
                    down = dp[row][col - 1]
                dp[row][col] = up + down
        return dp[m - 1][n -1]
        
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down with memo
        def calc_paths(m, n, dp):
            # Base case
            if m == 0 and n == 0:
                return 1
            if m < 0 or n < 0:
                return 0
            
            # Memoization Step
            if dp[m][n] != -1:
                return dp[m][n]
            
            # Accumulating while returning back
            #up = (-1,0)
            #down = (0,-1)
            up = calc_paths(m - 1, n, dp)
            down = calc_paths(m, n - 1, dp)
            dp[m][n] = (up + down)
            return dp[m][n]

        ROWS, COLS = m , n
        dp = [[-1] * (COLS + 1) for _ in range(ROWS)] # [[-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1]]
        return calc_paths(m - 1, n - 1, dp)
    
'''
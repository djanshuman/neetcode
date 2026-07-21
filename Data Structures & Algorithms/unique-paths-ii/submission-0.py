class Solution:
    # Bottom Up Approach with Memoization 
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        dp = [[-1] * (COLS) for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                if (row == 0 and col == 0) and obstacleGrid[row][col] != 1:
                    dp[row][col] = 1
                    continue

                if (row >= 0 or col >= 0) and (obstacleGrid[row][col] == 1):
                    dp[row][col] = 0
                    continue

                up = 0
                down = 0
                if row > 0:
                    up = dp[row - 1][col]
                if col > 0:
                    down = dp[row][col - 1]
                dp[row][col] = up + down

        return dp[ROWS - 1][COLS - 1]

'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # Top down with Memoization
        def calc_unique_paths(m , n, dp):
            # BASE CASE
            if (m == 0 and n == 0) and obstacleGrid[0][0] != 1:
                return 1
            # Out of bound case
            if (m < 0 or n < 0): 
                return 0 

            # Obstacle case   
            if (m >= 0 or n >= 0) and (obstacleGrid[m][n] == 1):
                return 0 

            if dp[m][n] != -1:
                return dp[m][n]

            up = calc_unique_paths(m - 1, n, dp)
            left = calc_unique_paths(m, n - 1, dp)
            dp[m][n] = up + left
            return dp[m][n]


        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        dp = [[-1] * (COLS + 1) for _ in range(ROWS)]
        return calc_unique_paths(ROWS - 1, COLS - 1, dp)
'''
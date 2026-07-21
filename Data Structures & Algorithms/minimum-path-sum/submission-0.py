class Solution:
    # Bottom up with Memo
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = [[-1] * (COLS + 1) for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 and col == 0:
                    dp[row][col] = grid[row][col]
                    continue
                up = float('inf')
                down = float('inf')
                if row > 0:
                    up = grid[row][col] + dp[row - 1][col]
                if col > 0:
                    down = grid[row][col] + dp[row][col - 1]

                dp[row][col] = min(up,down)
        return dp[ROWS - 1][COLS - 1]

                

    
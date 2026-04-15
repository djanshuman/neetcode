class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS , COLS = len(matrix) , len(matrix[0])

        # 1. Find the row which has the target and eliminate rows by setting top and bottom
        top , bot = 0 , ROWS - 1
        while (top <= bot):
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # 2. In case we are unable to find the exact row and invalid condition 
        if not (top <= bot):
            return False

        # 3. Using the top and bottom pointer , now lets do classic binary search to find the target

        row = (top + bot) // 2
        l , r = 0, COLS - 1

        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1

        return False


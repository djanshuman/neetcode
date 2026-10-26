'''
https://www.youtube.com/watch?v=rkLDDxOcJxU$0
'''

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.prefix_matrix = [[0] * (COLS + 1) for i in range(ROWS + 1)]

        #two pass approach to build row-wise and col wise prefix
        # each corner cell contains the sum from  (0,0)
        # the idea in suMRegion is to exclude extra part which is above and left.
        # top left gets excluded twice in left and above , so to counter , we add it again.
        # rows 
        for i in range(ROWS):
            prefix = 0
            for j in range(COLS):
                prefix = matrix[i][j] + prefix
                self.prefix_matrix[i + 1][j + 1] = prefix
        #print(self.prefix_matrix)
        #cols
        for j in range(COLS):
            prefix = 0
            for r in range(ROWS):
                prefix = self.prefix_matrix[r + 1][j + 1] + prefix
                self.prefix_matrix[r + 1][j + 1] = prefix
        #print(self.prefix_matrix)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    
        row1 = row1 + 1
        col1 = col1 + 1
        row2 = row2 + 1
        col2 = col2 + 1

        bottomright = self.prefix_matrix[row2][col2]
        above = self.prefix_matrix[row1 - 1 ][col2]
        topleft = self.prefix_matrix[row1 - 1 ][col1 - 1]
        left =  self.prefix_matrix[row2][col1 - 1]

        return bottomright - (above  + left) + topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
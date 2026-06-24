class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # STEP 1 : INITIALIZATION
        # Pacific Atlantic — the two-border version, and your reverse-flow logic is right (flood inward from each ocean, moving to cells of equal or higher height
        
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()

        # Bordering DFS 
        def dfs(row, col, visited, prev_height):
            if ((row,col) in visited or row < 0 or row == ROWS 
                or col < 0 or col == COLS
                or heights[row][col] < prev_height):
                return
            visited.add((row,col))
            dfs(row + 1 , col, visited,heights[row][col])
            dfs(row - 1 , col, visited,heights[row][col])
            dfs(row , col + 1, visited,heights[row][col])
            dfs(row , col - 1, visited,heights[row][col])



        #Check all columns for pacific and atlantic
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c , atl ,heights[ROWS - 1][c])

        #Check all rows for pacific and atlantic
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1 , atl ,heights[r][COLS - 1])

        #Check all the matrix cells which present in both pac and atl set
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

        
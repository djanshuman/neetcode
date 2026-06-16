from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows , num_cols = len(grid) , len(grid[0])

        # STEP 2 : DESIGN HELPER FUNC TO FETCH ADJACENT NEIGHBOUR 
        def get_neighbours(coord):
            row, col = coord
            delta_row = [-1,0,1,0]
            delta_col = [0,1,0,-1]
            for i in range(len(delta_row)):
                neighbour_row = row + delta_row[i]
                neighbour_col = col + delta_col[i]

                if 0 <= neighbour_row < num_rows and 0 <= neighbour_col < num_cols:
                    if grid[neighbour_row][neighbour_col] != "0":
                        yield neighbour_row , neighbour_col

        # STEP 3 : THE BFS ENGINE
        def bfs(root):
            q = deque([root])
            r , c = root
            grid[r][c] = "0" # mark it as visited

            while q:
                node = q.popleft()
                for neighbour in get_neighbours(node):
                    r , c = neighbour
                    if grid[r][c] == "0":
                        continue
                    grid[r][c] = "0"
                    q.append(neighbour)
        
        # STEP 1 : TRAVERSE THE GRID AND UPDATE COUNT PER ITERATION - IT COUNTS NO. OF CONNECTED COMPONENTS
        # NO OF TIMES START FRESH TRAVERSAL TO COVER ISLAND
        TOT_ISLAND = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "0":
                    continue
                bfs((r,c))
                TOT_ISLAND += 1

        return TOT_ISLAND
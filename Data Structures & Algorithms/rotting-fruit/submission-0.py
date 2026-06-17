from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #STEP 1 : INITIALIZATION
        fresh , time = 0, 0
        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])
        q = deque()


        #STEP 2: TRAVERSE THE MATRIX AND CAPTURE THE ROTTEN AND FRESH ORANGE
        # FRESH ORANGE - KEEP TRACK OF COUNT AND IF ANYTHING LEFT AT LAST THEN -1 RETURN
        # ENQUEUE ROTTEN ORANGE COORD TO QUEUE TO ENABLE MULTI SOURCE BFS

        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        
        #STEP 3 : TRAVERSE IN 4D AND EACH LEVEL ADD MINUTE
        directions = [[1 , 0] , [-1,0], [0,1], [0,-1]]
        while q and fresh > 0:
            lenq = len(q)
            for _ in range(lenq):
                r,c = q.popleft()
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    #Check if out of bounds and if not fresh
                    if (row < 0 or row == NUM_ROWS or 
                            col < 0 or col == NUM_COLS or
                            grid[row][col] != 1):
                            continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -=1
            time += 1

        return time if fresh == 0 else -1

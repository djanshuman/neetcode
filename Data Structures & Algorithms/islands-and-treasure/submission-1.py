class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #STEP 1: INITIALIZE VARIABLES
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()

        #STEP 3 : Helper function to validate adjacent neighbours and add to the queue
        # Rules : if out of bound or already visited or its a wall/obstacle 
        def addtoRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS 
                or (r,c) in visited or grid[r][c] == -1):
                return 
            q.append((r,c))
            visited.add((r,c))


        #STEP 2 : TRAVERSE THE MATRIX
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        
        #STEP 3: MAIN LOGIC OF BFS
        dist = 0
        while q:
            lenq = len(q)
            for _ in range(lenq):
                r , c = q.popleft()
                grid[r][c] = dist
                # perform multi-bfs across all 4D
                addtoRoom(r + 1, c)
                addtoRoom(r - 1, c)
                addtoRoom(r ,c + 1)
                addtoRoom(r ,c - 1)
            dist += 1

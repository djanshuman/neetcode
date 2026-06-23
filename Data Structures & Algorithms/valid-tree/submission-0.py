class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Edge case
        if not n:
            return True

        # Create adjacency list
        # {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}
        # {0: [1], 1: [0, 2, 3, 4], 2: [1, 3], 3: [2, 1], 4: [1]}
        adj = { i : [] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        print(adj)

        # use prev variable to keep track of root coming from.
        # if we are trying to dfs on already visited node then return False
        # prev will prevent from going back to parent as we are traversing neighbours
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for node in adj[i]:
                # prevent going to root from where coming
                if node == prev:
                    continue
                if not dfs(node,i):
                    return False
            return True 

        # if no loop and all are visited 
        return dfs(0, -1) and n == len(visited)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
        def find(x):
            if self.parent[x] == x:
                return x

            self.parent[x] = find(self.parent[x])
            return self.parent[x]


        def union(x,y):
            ax = find(x)
            ay = find(y)

            if ax == ay:
                return 0

            if self.rank[ax] < self.rank[ay]:
                self.parent[ax] = ay
                self.rank[ay] += self.rank[ax]
            else:
                self.parent[ay] = ax
                self.rank[ax] += self.rank[ay]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            ax = find(x)
            ay = find(y)

            if ax == ay:
                return False

            if rank[ax] < rank[ay]:
                parent[ax] = ay
                rank[ay] += rank[ax]
            else:
                parent[ay] = ax
                rank[ax] += rank[ay]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1,n2]
class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        ax = self.find(x)
        ay = self.find(y)

        if ax == ay:
            return
        
        if self.rank[ax] < self.rank[ay]:
            self.parent[ax] = ay
            self.rank[ay] += self.rank[ax]

        elif self.rank[ay] < self.rank[ax]:
            self.parent[ay] = ax
            self.rank[ax] += self.rank[ay]

        else:
            self.parent[ay] = ax
            self.rank[ax] += self.rank[ay]

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        #John ['johnsmith@mail.com', 'john_newyork@mail.com']
        #print(accounts[0][0], accounts[0][1:])

        uf = UnionFind(len(accounts))
        emailToAcc = {} # email to index of acc

        '''
        johnsmith@mail.com 0
        john_newyork@mail.com 0
        johnsmith@mail.com 1
        john00@mail.com 1
        mary@mail.com 2
        johnnybravo@mail.com 3

        Distinct mapping in emailToAcc
        {'johnsmith@mail.com': 0, 'john_newyork@mail.com': 0, 'john00@mail.com': 1, 'mary@mail.com': 2, 'johnnybravo@mail.com': 3}

        # This is the union and mapping operation to map same parent.
        uf.parent 
        [0 ,1 ,2 ,3] -> before union
        [1, 1, 2, 3] -> after union
        '''
        
        for i , a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list) #index of acc -> list of emails

        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        '''
        defaultdict(<class 'list'>, {1: ['johnsmith@mail.com', 'john_newyork@mail.com', 'john00@mail.com'], 2: ['mary@mail.com'], 3: ['johnnybravo@mail.com']})
        '''
        #print(emailGroup)
        res = []
        for i, e in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))

        return res





class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def isValid(x, k, l):
            for i in range(1, k):
                if (x[i] == l) or (abs(i - k) == abs(x[i] - l)):
                    return False
            return True

        def generateQueens(x, k, n, results):
            for i in range(1, n + 1):
                if isValid(x, k, i):
                    x[k] = i
                    if k == n:
                        board = []
                        for row in range(1, n + 1):
                            line = "." * (x[row] - 1) + "Q" + "." * (n - x[row])
                            board.append(line)
                        results.append(board)
                    else:
                        generateQueens(x, k + 1, n, results)

        x = [0] * (n + 1)
        results = []
        generateQueens(x, 1, n, results)
        return results
        

'''
k=1, i=1: valid → x=[0,1,0,0,0]
  k=2, i=1: col conflict → skip
  k=2, i=2: diag conflict → skip
  k=2, i=3: valid → x=[0,1,3,0,0]
    k=3, i=1: diag conflict → skip
    k=3, i=2: diag conflict → skip
    k=3, i=3: col conflict → skip
    k=3, i=4: diag conflict → skip
    → return
  k=2, i=4: valid → x=[0,1,4,0,0]
    k=3, i=1: diag conflict → skip
    k=3, i=2: valid → x=[0,1,4,2,0]
      k=4, i=1: diag conflict → skip
      k=4, i=2: col conflict → skip
      k=4, i=3: diag conflict → skip
      k=4, i=4: col conflict → skip
      → return
    k=3, i=3: diag conflict → skip
    k=3, i=4: col conflict → skip
    → return

k=1, i=2: valid → x=[0,2,0,0,0]
  k=2, i=1: diag conflict → skip
  k=2, i=2: col conflict → skip
  k=2, i=3: diag conflict → skip
  k=2, i=4: valid → x=[0,2,4,0,0]
    k=3, i=1: valid → x=[0,2,4,1,0]
      k=4, i=1: col conflict → skip
      k=4, i=2: col conflict → skip
      k=4, i=3: valid → x=[0,2,4,1,3]  ← SOLUTION
        .Q..
        ...Q
        Q...
        ..Q.
      k=4, i=4: diag conflict → skip
    k=3, i=2: col conflict → skip
    k=3, i=3: diag conflict → skip
    k=3, i=4: col conflict → skip

k=1, i=3: valid → x=[0,3,0,0,0]
  k=2, i=1: valid → x=[0,3,1,0,0]
    k=3, i=1: col conflict → skip
    k=3, i=2: diag conflict → skip
    k=3, i=3: col conflict → skip
    k=3, i=4: valid → x=[0,3,1,4,0]
      k=4, i=1: diag conflict → skip
      k=4, i=2: valid → x=[0,3,1,4,2]  ← SOLUTION
        ..Q.
        Q...
        ...Q
        .Q..
      k=4, i=3: col conflict → skip
      k=4, i=4: col conflict → skip
  k=2, i=2: diag conflict → skip
  k=2, i=3: col conflict → skip
  k=2, i=4: diag conflict → skip
  '''
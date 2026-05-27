# Last updated: 5/27/2026, 11:01:19 AM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3
4        def solve(col):
5            if col == n:
6                res.append(["".join(r) for r in board])
7                return
8            
9            for row in range(n):
10                if left[row] == 0 and bottomDiagonal[row + col] == 0 and topDiagonal[(n - 1 )+ (col - row)] == 0:
11                    board[row][col] = "Q"
12                    left[row] = 1
13                    bottomDiagonal[row + col] = 1
14                    topDiagonal[(n - 1) + (col - row)] = 1
15
16                    solve(col + 1)
17
18                    board[row][col] = "."
19                    left[row] = 0
20                    bottomDiagonal[row + col] = 0
21                    topDiagonal[(n - 1) + (col - row)] = 0
22
23
24        res = []
25        board = [['.'] * n for _ in range(n)]
26        left = [0] * n
27        bottomDiagonal = [0] * (2 * n - 1)
28        topDiagonal = [0] * (2 * n - 1)
29
30        solve(0)
31        return res
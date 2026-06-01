# Last updated: 6/1/2026, 6:14:07 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        if not board or not board[0]:
4            return
5
6        rows, cols = len(board), len(board[0])
7
8        def dfs(r, c):
9            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "X" or board[r][c] == "S":
10                return 
11
12            board[r][c] = "S"
13
14            dfs(r + 1, c)
15            dfs(r - 1, c)
16            dfs(r, c + 1)
17            dfs(r, c - 1)
18
19        for r in range(rows):
20            dfs(r, 0)
21            dfs(r, cols - 1)
22        
23        for c in range(cols):
24            dfs(0, c)
25            dfs(rows - 1, c)
26
27
28        for i in range(rows):
29            for j in range(cols):
30                if board[i][j] == "S":
31                    board[i][j] = "O"
32                elif board[i][j] == "O":
33                    board[i][j] = "X"
34
35        return board
36        
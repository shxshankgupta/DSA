# Last updated: 5/26/2026, 6:54:50 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        rows = len(board)
4        cols = len(board[0])
5
6        def back(r, c, i):
7            if i == len(word):
8                return True
9            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == '$' or board[r][c] != word[i]:
10                return False
11            
12            temp = board[r][c]
13            board[r][c] = '$'
14            res = back(r+1, c, i+1) or back(r-1, c, i+1) or back(r, c+1, i+1) or back(r, c-1, i+1)
15            board[r][c] = temp
16            return res
17
18        for r in range(rows):
19            for c in range(cols):
20                if board[r][c] == word[0] and back (r, c, 0):
21                    return True
22            
23        return False
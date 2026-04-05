# Last updated: 4/5/2026, 10:33:24 AM
1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        x = 0
4        y = 0
5        for move in moves:
6            if move == 'U':
7                y += 1
8            elif move == 'D':
9                y -= 1
10            elif move == 'R':
11                x += 1
12            else:
13                x -= 1
14        
15        return x == 0 and y == 0
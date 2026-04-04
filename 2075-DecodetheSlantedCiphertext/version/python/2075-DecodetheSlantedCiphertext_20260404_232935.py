# Last updated: 4/4/2026, 11:29:35 PM
1class Solution:
2    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
3        if not encodedText:
4            return ""
5        
6        n = len(encodedText)
7        cols = n // rows
8        res = []
9        
10        for i in range(cols):
11            r, c = 0, i
12            while r < rows and c < cols:
13                res.append(encodedText[r * cols + c])
14                r += 1
15                c += 1
16        
17        return "".join(res).rstrip()
# Last updated: 6/22/2026, 8:52:11 AM
1class Solution:
2    def maxNumberOfBalloons(self, text: str) -> int:
3        
4        b = 0
5        a = 0
6        l = 0
7        o = 0
8        n = 0
9        
10        for char in text:
11            if char == 'b':
12                b += 1
13            elif char == 'a':
14                a += 1
15            elif char == 'l':
16                l += 1
17            elif char == 'o':
18                o += 1
19            elif char == 'n':
20                n += 1
21                
22        l = l // 2
23        o = o // 2
24        
25        return min(b, a, l, o, n)
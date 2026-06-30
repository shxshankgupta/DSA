# Last updated: 6/30/2026, 9:55:27 AM
1class Solution:
2    def numberOfSubstrings(self, s: str) -> int:
3        n = len(s)
4        res = 0
5        abc =[0] * 3
6
7        left = 0
8
9        for right in range(n):
10            if s[right] == 'a':
11                abc[0] += 1
12            elif s[right] == 'b':
13                abc[1] += 1
14            else:
15                abc[2] += 1
16
17            while abc[0] > 0 and abc[1] > 0 and abc[2] > 0:
18                res += n - right
19
20                if s[left] == 'a':
21                    abc[0] -= 1
22                elif s[left] == 'b':
23                    abc[1] -= 1
24                else:
25                    abc[2] -= 1
26                
27                left += 1
28        
29        return res
30        
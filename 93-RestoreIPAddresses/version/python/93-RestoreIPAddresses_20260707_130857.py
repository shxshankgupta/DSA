# Last updated: 7/7/2026, 1:08:57 PM
1class Solution:
2    def restoreIpAddresses(self, s: str) -> list[str]:
3        n = len(s)
4        if n > 12:
5            return []
6        
7        result = []
8        
9        def is_valid(string: str) -> bool:
10            if string[0] == '0' and len(string) > 1:
11                return False
12            
13            val = int(string)
14            return val <= 255
15
16        def solve(idx: int, parts: int, current: str):
17            if idx == n and parts == 4:
18                result.append(current[:-1])
19                return
20            
21            if parts >= 4:
22                return
23
24            if idx + 1 <= n:
25                solve(idx + 1, parts + 1, current + s[idx:idx+1] + ".")
26
27            if idx + 2 <= n and is_valid(s[idx:idx+2]):
28                solve(idx + 2, parts + 1, current + s[idx:idx+2] + ".")
29
30            if idx + 3 <= n and is_valid(s[idx:idx+3]):
31                solve(idx + 3, parts + 1, current + s[idx:idx+3] + ".")
32
33        solve(0, 0, "")
34        return result
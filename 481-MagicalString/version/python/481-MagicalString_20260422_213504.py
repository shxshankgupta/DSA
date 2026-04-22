# Last updated: 4/22/2026, 9:35:04 PM
1class Solution:
2    def magicalString(self, n: int) -> int:
3        if n <= 0: return 0
4        if n <= 3: return 1  
5        
6        s = [1, 2, 2]
7        head = 2  
8        while len(s) < n:
9            next_num = 3 - s[-1]
10            
11            count = s[head]
12            
13            for _ in range(count):
14                if len(s) < n:
15                    s.append(next_num)
16            
17            head += 1
18            
19        return s.count(1)
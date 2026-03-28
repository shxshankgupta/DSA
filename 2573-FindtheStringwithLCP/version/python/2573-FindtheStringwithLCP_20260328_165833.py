# Last updated: 3/28/2026, 4:58:33 PM
1class Solution:
2    def findTheString(self, lcp: List[List[int]]) -> str:
3        n = len(lcp)
4        res = [0] * n
5        char_code = 1
6        
7        for i in range(n):
8            if res[i] > 0: continue
9            if char_code > 26: return "" 
10            
11            for j in range(i, n):
12                if lcp[i][j] > 0:
13                    res[j] = char_code
14            char_code += 1
15        
16        word = "".join(chr(ord('a') + c - 1) for c in res)
17        
18        for i in range(n - 1, -1, -1):
19            for j in range(n - 1, -1, -1):
20                expected = 0
21                if word[i] == word[j]:
22                    expected = 1 + (lcp[i+1][j+1] if (i + 1 < n and j + 1 < n) else 0)
23                
24                if lcp[i][j] != expected:
25                    return ""
26                    
27        return word
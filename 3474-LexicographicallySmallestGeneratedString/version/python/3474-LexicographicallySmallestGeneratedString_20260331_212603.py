# Last updated: 3/31/2026, 9:26:03 PM
1class Solution:
2    def generateString(self, str1: str, str2: str) -> str:
3        n, m = len(str1), len(str2)
4        total_len = n + m - 1
5        word = [None] * total_len
6        
7        for i in range(n):
8            if str1[i] == 'T':
9                for j in range(m):
10                    if word[i + j] is not None and word[i + j] != str2[j]:
11                        return "" 
12                    word[i + j] = str2[j]
13    
14        res = list(word)
15        for i in range(total_len):
16            if res[i] is None:
17                res[i] = 'a'
18
19        fixed = [False] * total_len
20        for i in range(n):
21            if str1[i] == 'T':
22                for j in range(m):
23                    fixed[i + j] = True
24                    
25        for i in range(n):
26            if str1[i] == 'F':
27                match = True
28                for j in range(m):
29                    if res[i + j] != str2[j]:
30                        match = False
31                        break
32                
33                if match:
34                    changed = False
35                    for j in range(m - 1, -1, -1):
36                        if not fixed[i + j]:
37                            for char_code in range(ord('a'), ord('z') + 1):
38                                char = chr(char_code)
39                                if char != str2[j]:
40                                    res[i + j] = char
41                                    changed = True
42                                    break
43                        if changed: break
44                    
45                    if not changed: return ""
46        
47        for i in range(n):
48            curr_sub = "".join(res[i:i+m])
49            if (str1[i] == 'T' and curr_sub != str2) or (str1[i] == 'F' and curr_sub == str2):
50                return ""
51                
52        return "".join(res)
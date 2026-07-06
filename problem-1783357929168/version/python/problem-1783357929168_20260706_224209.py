# Last updated: 7/6/2026, 10:42:09 PM
1class Solution:
2    def halvesAreAlike(self, s: str) -> bool:
3        vowels = set("aeiouAEIOU")
4
5        n = len(s)
6        half = n//2
7
8        c1 = 0
9        c2 = 0
10
11        i, j = 0, half
12
13        while i<half and j < n:
14            if s[i] in vowels:
15                c1 += 1
16            if s[j] in vowels:
17                c2 += 1
18
19            i += 1
20            j += 1
21
22        return c1 == c2
23            
24
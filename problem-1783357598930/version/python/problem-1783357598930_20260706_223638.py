# Last updated: 7/6/2026, 10:36:38 PM
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
11        a = s[:half]
12        b = s[half:]
13
14        for char in a:
15            if char in vowels:
16                c1 += 1
17        
18        for char in b:
19            if char in vowels:
20                c2 += 1
21
22        return c1 == c2
23            
24
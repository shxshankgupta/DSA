# Last updated: 3/30/2026, 10:57:28 PM
1from collections import Counter
2
3class Solution:
4    def checkStrings(self, s1: str, s2: str) -> bool:
5        # Compare characters at even indices
6        even_s1 = Counter(s1[0::2])
7        even_s2 = Counter(s2[0::2])
8        
9        # Compare characters at odd indices
10        odd_s1 = Counter(s1[1::2])
11        odd_s2 = Counter(s2[1::2])
12        
13        return even_s1 == even_s2 and odd_s1 == odd_s2
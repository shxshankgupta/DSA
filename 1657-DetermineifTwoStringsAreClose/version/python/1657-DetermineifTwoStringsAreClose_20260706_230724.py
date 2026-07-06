# Last updated: 7/6/2026, 11:07:24 PM
1from collections import Counter
2class Solution:
3    def closeStrings(self, word1: str, word2: str) -> bool:
4        if len(word1) != len(word2):
5            return False
6        
7        s1 = set(word1)
8        s2 = set(word2)
9
10        if s1 != s2:
11            return False
12        
13        l1 = [0] * 26
14        l2 = [0] * 26
15
16        for char in word1:
17            l1[ord(char) - ord('a')] += 1
18        
19        for char in word2:
20            l2[ord(char) - ord('a')] += 1
21
22        if sorted(l1) == sorted(l2):
23            return True
24
25        return False
26        
27
28
29
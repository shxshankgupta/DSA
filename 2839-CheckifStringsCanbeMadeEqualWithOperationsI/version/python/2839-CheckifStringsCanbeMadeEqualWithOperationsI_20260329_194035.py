# Last updated: 3/29/2026, 7:40:35 PM
1class Solution:
2    def canBeEqual(self, s1: str, s2: str) -> bool:
3        even_match = (s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2] and s1[2] == s2[0])
4        odd_match = (s1[1] == s2[1] and s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1])
5        return even_match and odd_match
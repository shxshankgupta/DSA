# Last updated: 5/26/2026, 11:11:28 AM
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        char_set = set(word)
4        count = 0
5        
6        for char in char_set:
7            if char.islower() and char.upper() in char_set:
8                count += 1
9                
10        return count
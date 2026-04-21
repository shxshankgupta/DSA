# Last updated: 4/21/2026, 6:42:17 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        if not s or len(s) < 1:
4            return ""
5        
6        start, end = 0, 0
7        
8        for i in range(len(s)):
9            len1 = self.expandAroundCenter(s, i, i)
10            len2 = self.expandAroundCenter(s, i, i + 1)
11            
12            max_len = max(len1, len2)
13            
14            if max_len > (end - start):
15                start = i - (max_len - 1) // 2
16                end = i + max_len // 2
17                
18        return s[start : end + 1]
19
20    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
21        while left >= 0 and right < len(s) and s[left] == s[right]:
22            left -= 1
23            right += 1
24        
25        return right - left - 1
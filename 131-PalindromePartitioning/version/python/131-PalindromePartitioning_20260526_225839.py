# Last updated: 5/26/2026, 10:58:39 PM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        res, sol = [], []
4        n = len(s)
5
6        def back(idx):
7            if idx == n:
8                res.append(list(sol))
9                return
10        
11            for i in range(idx, n):
12                if self.isPalindrome(s, idx, i):
13                    sol.append(s[idx : i + 1])
14                    back(i+1)
15                    sol.pop()
16
17        back(0)
18        return res
19
20    def isPalindrome(self, s, l, r):
21            while l < r:
22                if s[l] != s[r]:
23                    return False
24                l += 1
25                r -= 1    
26            return True
27
28
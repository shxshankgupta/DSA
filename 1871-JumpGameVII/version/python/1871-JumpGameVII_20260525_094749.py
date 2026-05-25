# Last updated: 5/25/2026, 9:47:49 AM
1class Solution:
2    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
3        n = len(s)
4        if s[n - 1] == '1':
5            return False
6            
7        dp = [False] * n
8        dp[0] = True
9        reachable_count = 0
10        
11        for i in range(1, n):
12            if i >= minJump:
13                if dp[i - minJump]:
14                    reachable_count += 1
15            if i > maxJump:
16                if dp[i - maxJump - 1]:
17                    reachable_count -= 1
18                    
19            if s[i] == '0' and reachable_count > 0:
20                dp[i] = True
21                
22        return dp[n - 1]
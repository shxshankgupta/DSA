# Last updated: 6/20/2026, 9:48:45 PM
1class Solution:
2    def totalWaviness(self, num1: int, num2: int) -> int:
3        
4        def get_waviness(limit_str: str) -> int:
5            n = len(limit_str)
6            memo = {}
7            
8            def dp(i, tight, last, prev, leading):
9                if i == n:
10                    return 0, 1
11                
12                state = (i, tight, last, prev, leading)
13                if state in memo:
14                    return memo[state]
15                
16                limit = int(limit_str[i]) if tight else 9
17                res_waviness = 0
18                res_count = 0
19                
20                for d in range(limit + 1):
21                    nxt_tight = tight and (d == limit)
22                    nxt_leading = leading and (d == 0)
23                    
24                    curr_waviness = 0
25                    if not leading and prev != 10 and last != 10:
26                        if (last > prev and last > d) or (last < prev and last < d):
27                            curr_waviness = 1
28                    
29                    next_last = 10 if nxt_leading else d
30                    next_prev = 10 if nxt_leading else last
31                    
32                    sub_waviness, sub_count = dp(i + 1, nxt_tight, next_last, next_prev, nxt_leading)
33                    
34                    res_waviness += sub_waviness + (curr_waviness * sub_count)
35                    res_count += sub_count
36                    
37                memo[state] = (res_waviness, res_count)
38                return memo[state]
39            
40            return dp(0, True, 10, 10, True)[0]
41
42        return get_waviness(str(num2)) - get_waviness(str(num1 - 1))
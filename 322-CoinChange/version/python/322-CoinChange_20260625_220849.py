# Last updated: 6/25/2026, 10:08:49 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        dp = [-1] * (amount + 1) 
4        def solve(rem_amt):
5            if rem_amt == 0:
6                return 0
7            
8            if rem_amt < 0:
9                return float('inf')
10
11            if dp[rem_amt] != -1:
12                return dp[rem_amt]
13
14            min_coins = float('inf')
15
16            for coin in coins:
17                res = solve(rem_amt - coin)
18
19                if res != float('inf'):
20                    min_coins = min(min_coins, 1 + res)
21
22            dp[rem_amt] = min_coins
23
24            return dp[rem_amt]
25
26        ans = solve(amount)
27
28        return ans if ans != float('inf') else -1
29
30
31        
32
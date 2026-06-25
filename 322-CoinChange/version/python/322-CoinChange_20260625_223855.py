# Last updated: 6/25/2026, 10:38:55 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        dp = [amount + 1] * (amount + 1) 
4        dp[0] = 0
5
6        for i in range(1, amount+1):
7            for coin in coins:
8                if i - coin >= 0:
9                    dp[i] = min(dp[i], 1 + dp[i - coin])
10
11        return dp[amount] if dp[amount] != amount + 1 else -1
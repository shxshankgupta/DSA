# Last updated: 6/27/2026, 5:34:36 PM
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9+7
        dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
        for j in range(1, m+1):
            dp[1][j][1] = 1
        for a in range(1,n+1):
            for b in range(1,m+1):
                for c in range(1,k+1):
                    s = 0
                    s += b * dp[a-1][b][c] % MOD
                    for x in range(1, b):
                        s += dp[a-1][x][c-1] % MOD
                    dp[a][b][c] += s % MOD
        return sum(dp[n][x][k] for x in range(1, m+1)) % MOD
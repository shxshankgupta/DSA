# Last updated: 7/8/2026, 8:05:49 PM
1class Solution:
2    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
3        result = []
4        MOD = 10**9 + 7
5
6        n = len(s)
7        
8        num = [0] * (n+1)
9        dig_sum = [0] * (n+1)
10        non_zero = [0] * (n+1)
11
12        for i in range(len(s)):
13            dig = int(s[i])
14            
15            dig_sum[i+1] = dig_sum[i] + dig
16
17            if dig != 0:
18                num[i+1] = ((num[i]*10) + dig) % MOD
19                non_zero[i+1] = non_zero[i] + 1
20            else:
21                num[i+1] = num[i]
22                non_zero[i+1] = non_zero[i]
23
24        for query in queries:
25            l, r = query[0], query[1] + 1
26            qr_sum = dig_sum[r] - dig_sum[l]
27            k = non_zero[r] - non_zero[l]
28
29            qr_num = num[r] - (num[l] * pow(10, k, MOD))
30            res = (qr_num * qr_sum) % MOD
31            result.append(res)
32
33        return result
34
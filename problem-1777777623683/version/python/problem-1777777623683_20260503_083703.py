# Last updated: 5/3/2026, 8:37:03 AM
1class Solution:
2    def sumOfPrimesInRange(self, n: int) -> int:
3        
4        r = int(str(n)[::-1])
5 
6        # 2. Prime check karne ke liye Helper Function
7        def is_prime(num):
8            if num < 2:
9                return False
10            for i in range(2, int(num**0.5) + 1):
11                if num % i == 0:
12                    return False
13            return True
14    
15        total_sum = 0
16        for i in range(min(n, r), max(n, r) + 1):
17            if is_prime(i):
18                total_sum += i
19        
20        return total_sum
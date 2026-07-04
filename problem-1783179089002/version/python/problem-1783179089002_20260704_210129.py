# Last updated: 7/4/2026, 9:01:29 PM
1class Solution:
2    def minOperations(self, s1: str, s2: str) -> int:
3        n = len(s1)
4        if s1 == s2:
5            return 0
6        if not self.is_feasible(s1, s2, n):
7            return -1
8        return self.count_min_ops(s1, s2, n)
9
10    def is_feasible(self, s1: str, s2: str, n: int) -> bool:
11        # The ONLY impossible case: a single lone '1' that needs to become '0'
12        # with no neighbor to pair with (op2 needs two adjacent 1s).
13        if n == 1:
14            return s1[0] == s2[0] or s1[0] == '0'
15        return True
16
17    def count_min_ops(self, s1: str, s2: str, n: int) -> int:
18        plus_count = 0    # positions needing 0 -> 1 (direct op1, cost 1 each)
19        pair_count = 0    # adjacent "need 1->0" pairs, cost 1 per PAIR (op2)
20        unpaired_count = 0  # leftover lone "need 1->0", cost 2 each (borrow + fix)
21
22        i = 0
23        while i < n:
24            if s1[i] == s2[i]:
25                i += 1
26                continue
27            if s1[i] == '0':  # and s2[i] == '1'
28                plus_count += 1
29                i += 1
30            else:
31                # s1[i]=='1', s2[i]=='0': start of a run of consecutive "off" spots
32                run_start = i
33                while i < n and s1[i] == '1' and s2[i] == '0':
34                    i += 1
35                run_len = i - run_start
36                pair_count += run_len // 2
37                unpaired_count += run_len % 2
38
39        return plus_count + pair_count + unpaired_count * 2
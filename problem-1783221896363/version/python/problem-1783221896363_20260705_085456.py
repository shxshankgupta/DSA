# Last updated: 7/5/2026, 8:54:56 AM
1class Solution:
2    def canMakeSubsequence(self, s: str, t: str) -> bool:
3        n = len(s)
4        m = len(t)
5
6        # Already a subsequence
7        i = j = 0
8        while i < n and j < m:
9            if s[i] == t[j]:
10                i += 1
11            j += 1
12        if i == n:
13            return True
14
15        # pref[i] = matched chars of s using t[:i]
16        pref = [0] * (m + 1)
17        i = 0
18        for j in range(m):
19            if i < n and s[i] == t[j]:
20                i += 1
21            pref[j + 1] = i
22
23        # suff[i] = starting index in s that can still be matched using t[i:]
24        suff = [0] * (m + 1)
25        i = n - 1
26        suff[m] = i
27        for j in range(m - 1, -1, -1):
28            if i >= 0 and s[i] == t[j]:
29                i -= 1
30            suff[j] = i
31
32        for pos in range(m):
33            left = pref[pos]
34            if left >= n:
35                return True
36            if suff[pos + 1] <= left:
37                return True
38
39        return False
# Last updated: 3/14/2026, 10:01:17 PM
1import bisect
2
3class TimeMap:
4
5    def __init__(self):
6        # Dictionary to store key -> list of [timestamp, value]
7        self.store = {}
8
9    def set(self, key: str, value: str, timestamp: int) -> None:
10        if key not in self.store:
11            self.store[key] = []
12        # Since timestamps are strictly increasing, 
13        # we can just append to the list.
14        self.store[key].append([timestamp, value])
15
16    def get(self, key: str, timestamp: int) -> str:
17        if key not in self.store:
18            return ""
19        
20        values = self.store[key]
21        
22        # Binary search to find the position where 'timestamp' 
23        # would be inserted to maintain order.
24        # We use a dummy list [timestamp, chr(127)] to compare 
25        # against [t, v] pairs.
26        idx = bisect.bisect_right(values, [timestamp, chr(127)])
27        
28        # If idx is 0, no timestamp_prev <= timestamp exists.
29        if idx == 0:
30            return ""
31        
32        # Return the value at the found index - 1
33        return values[idx - 1][1]
34
35# Your TimeMap object will be instantiated and called as such:
36# obj = TimeMap()
37# obj.set(key,value,timestamp)
38# param_2 = obj.get(key,timestamp)
39
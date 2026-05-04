# Last updated: 5/4/2026, 10:54:10 PM
1import heapq
2
3class KthLargest:
4    def __init__(self, k: int, nums: List[int]):
5        self.k = k
6        self.min_heap = nums
7        heapq.heapify(self.min_heap)
8      
9        while len(self.min_heap) > k:
10            heapq.heappop(self.min_heap)
11
12    def add(self, val: int) -> int:
13        heapq.heappush(self.min_heap, val)
14        
15        if len(self.min_heap) > self.k:
16            heapq.heappop(self.min_heap)
17            
18        return self.min_heap[0]
19
20
21# Your KthLargest object will be instantiated and called as such:
22# obj = KthLargest(k, nums)
23# param_1 = obj.add(val)
# Last updated: 4/11/2026, 10:19:16 PM
1class Node:
2    def __init__(self, key, value):
3        self.key = key
4        self.val = value
5        self.prev = None
6        self.next = None
7
8class LRUCache:
9    def __init__(self, capacity: int):
10        self.cap = capacity
11        self.cache = {}  
12        self.head = Node(0, 0)
13        self.tail = Node(0, 0)
14        self.head.next = self.tail
15        self.tail.prev = self.head
16
17    def _remove(self, node):
18        """Remove an existing node from the linked list."""
19        prev, nxt = node.prev, node.next
20        prev.next, nxt.prev = nxt, prev
21
22    def _add(self, node):
23        """Insert a new node right after the head (MRU position)."""
24        nxt = self.head.next
25        self.head.next = node
26        node.prev = self.head
27        node.next = nxt
28        nxt.prev = node
29
30    def get(self, key: int) -> int:
31        if key in self.cache:
32            node = self.cache[key]
33            self._remove(node)
34            self._add(node)
35            return node.val
36        return -1
37
38    def put(self, key: int, value: int) -> None:
39        if key in self.cache:
40            self._remove(self.cache[key])
41        
42        new_node = Node(key, value)
43        self.cache[key] = new_node
44        self._add(new_node)
45        
46        if len(self.cache) > self.cap:
47            lru = self.tail.prev
48            self._remove(lru)
49            del self.cache[lru.key]
50
51# Your LRUCache object will be instantiated and called as such:
52# obj = LRUCache(capacity)
53# param_1 = obj.get(key)
54# obj.put(key,value)
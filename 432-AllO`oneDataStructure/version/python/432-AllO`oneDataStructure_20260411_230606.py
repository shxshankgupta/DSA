# Last updated: 4/11/2026, 11:06:06 PM
1class Node:
2    def __init__(self, count):
3        self.count = count
4        self.keys = set()
5        self.prev = None
6        self.next = None
7
8class AllOne:
9    def __init__(self):
10        self.map = {}  
11        self.head = Node(0)
12        self.tail = Node(0)
13        self.head.next = self.tail
14        self.tail.prev = self.head
15
16    def _add_node_after(self, new_node, prev_node):
17        new_node.prev = prev_node
18        new_node.next = prev_node.next
19        prev_node.next.prev = new_node
20        prev_node.next = new_node
21
22    def _remove_node(self, node):
23        node.prev.next = node.next
24        node.next.prev = node.prev
25
26    def inc(self, key: str) -> None:
27        if key not in self.map:
28            if self.head.next.count != 1:
29                self._add_node_after(Node(1), self.head)
30            self.head.next.keys.add(key)
31            self.map[key] = self.head.next
32        else:
33            cur_node = self.map[key]
34            next_count = cur_node.count + 1
35            if cur_node.next.count != next_count:
36                self._add_node_after(Node(next_count), cur_node)
37            
38            cur_node.next.keys.add(key)
39            self.map[key] = cur_node.next
40            cur_node.keys.remove(key)
41            if not cur_node.keys:
42                self._remove_node(cur_node)
43
44    def dec(self, key: str) -> None:
45        cur_node = self.map[key]
46        if cur_node.count == 1:
47            del self.map[key]
48        else:
49            prev_count = cur_node.count - 1
50            if cur_node.prev.count != prev_count:
51                self._add_node_after(Node(prev_count), cur_node.prev)
52            
53            cur_node.prev.keys.add(key)
54            self.map[key] = cur_node.prev
55        
56        cur_node.keys.remove(key)
57        if not cur_node.keys:
58            self._remove_node(cur_node)
59
60    def getMaxKey(self) -> str:
61        if self.tail.prev == self.head:
62            return ""
63        return next(iter(self.tail.prev.keys))
64
65    def getMinKey(self) -> str:
66        if self.head.next == self.tail:
67            return ""
68        return next(iter(self.head.next.keys))
69
70# Your AllOne object will be instantiated and called as such:
71# obj = AllOne()
72# obj.inc(key)
73# obj.dec(key)
74# param_3 = obj.getMaxKey()
75# param_4 = obj.getMinKey()
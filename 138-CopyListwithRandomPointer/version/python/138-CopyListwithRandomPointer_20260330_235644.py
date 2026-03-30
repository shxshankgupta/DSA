# Last updated: 3/30/2026, 11:56:44 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        if not head:
13            return None
14        
15        old_to_new = {None: None}
16        
17        curr = head
18        while curr:
19            old_to_new[curr] = Node(curr.val)
20            curr = curr.next
21            
22        curr = head
23        while curr:
24            copy = old_to_new[curr]
25            copy.next = old_to_new[curr.next]
26            copy.random = old_to_new[curr.random]
27            curr = curr.next
28            
29        return old_to_new[head]
30        
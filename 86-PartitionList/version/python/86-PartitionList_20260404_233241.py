# Last updated: 4/4/2026, 11:32:41 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
9        less_head = ListNode(0)
10        greater_head = ListNode(0)
11        
12        less = less_head
13        greater = greater_head
14        
15        curr = head
16        while curr:
17            if curr.val < x:
18                less.next = curr
19                less = less.next
20            else:
21                greater.next = curr
22                greater = greater.next
23            curr = curr.next
24        
25        greater.next = None
26        
27        less.next = greater_head.next
28        
29        return less_head.next
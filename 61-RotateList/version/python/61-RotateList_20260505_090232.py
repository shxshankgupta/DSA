# Last updated: 5/5/2026, 9:02:32 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
9        if not head or not head.next or k == 0:
10            return head
11    
12        old_tail = head
13        length = 1
14        while old_tail.next:
15            old_tail = old_tail.next
16            length += 1
17
18        old_tail.next = head
19
20        k = k % length
21        new_tail_steps = length - k - 1
22        
23        new_tail = head
24        for _ in range(new_tail_steps):
25            new_tail = new_tail.next
26            
27        new_head = new_tail.next
28        
29        new_tail.next = None
30        
31        return new_head
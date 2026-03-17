# Last updated: 3/17/2026, 10:54:46 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        slow = head
10        fast = head
11        
12        while fast and fast.next:
13            slow = slow.next          
14            fast = fast.next.next     
15            
16            if slow == fast:
17                return True
18        
19        return False
# Last updated: 4/21/2026, 6:51:14 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6# Definition for singly-linked list.
7# class ListNode:
8#     def __init__(self, val=0, next=None):
9#         self.val = val
10#         self.next = next
11
12class Solution:
13    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
14        current = head
15        
16        while current and current.next:
17            if current.val == current.next.val:
18                current.next = current.next.next
19            else:
20                current = current.next
21                
22        return head
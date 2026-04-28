# Last updated: 4/28/2026, 11:49:01 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        dummy = ListNode(0, head)
10        prev = dummy
11        
12        while head:
13            if head.next and head.val == head.next.val:
14                while head.next and head.val == head.next.val:
15                    head = head.next
16                prev.next = head.next 
17            else:
18                prev = prev.next
19
20            head = head.next
21            
22        return dummy.next
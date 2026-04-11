# Last updated: 4/11/2026, 11:20:25 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(0)
9        dummy.next = head
10        current = dummy
11        
12        while current.next and current.next.next:
13            first = current.next
14            second = current.next.next
15            
16            first.next = second.next
17            second.next = first
18            current.next = second
19            
20            current = first
21            
22        return dummy.next
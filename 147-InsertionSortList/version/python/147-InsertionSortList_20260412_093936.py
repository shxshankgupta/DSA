# Last updated: 4/12/2026, 9:39:36 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        if not head or not head.next:
10            return head
11        
12        dummy = ListNode(0)
13        dummy.next = head
14        last_sorted = head 
15        curr = head.next
16        
17        while curr:
18            if last_sorted.val <= curr.val:
19                last_sorted = last_sorted.next
20            else:
21                prev = dummy
22                while prev.next.val <= curr.val:
23                    prev = prev.next
24                
25                last_sorted.next = curr.next
26                curr.next = prev.next
27                prev.next = curr
28                
29            curr = last_sorted.next
30            
31        return dummy.next
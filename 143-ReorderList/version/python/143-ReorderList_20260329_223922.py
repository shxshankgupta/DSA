# Last updated: 3/29/2026, 10:39:22 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reorderList(self, head: Optional[ListNode]) -> None:
9        if not head or not head.next:
10            return
11
12        slow, fast = head, head.next
13        while fast and fast.next:
14            slow = slow.next
15            fast = fast.next.next
16        
17        second = slow.next
18        slow.next = None 
19
20        prev = None
21        while second:
22            tmp = second.next
23            second.next = prev
24            prev = second
25            second = tmp
26        
27        first, second = head, prev
28        while second:
29            tmp1, tmp2 = first.next, second.next
30            first.next = second
31            second.next = tmp1
32            first, second = tmp1, tmp2        
33
34            
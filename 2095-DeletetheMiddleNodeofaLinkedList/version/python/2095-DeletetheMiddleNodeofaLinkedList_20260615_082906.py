# Last updated: 6/15/2026, 8:29:06 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        if not head or not head.next:
10            return None
11
12        slow = head
13        fast = head
14        prev = None
15
16        while fast and fast.next:
17            prev = slow
18            slow = slow.next
19            fast = fast.next.next
20
21        prev.next = slow.next
22
23        return head
# Last updated: 4/12/2026, 11:37:59 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def isPalindrome(self, head: Optional[ListNode]) -> bool:
8        if not head or not head.next:
9            return True
10        
11        slow = fast = head
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15            
16        prev = None
17        curr = slow
18        while curr:
19            next_node = curr.next
20            curr.next = prev
21            prev = curr
22            curr = next_node
23            
24        left, right = head, prev
25        while right: 
26            if left.val != right.val:
27                return False
28            left = left.next
29            right = right.next
30            
31        return True
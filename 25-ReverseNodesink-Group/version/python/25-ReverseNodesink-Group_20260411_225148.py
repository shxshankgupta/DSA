# Last updated: 4/11/2026, 10:51:48 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head or k == 1:
9            return head
10        
11        dummy = ListNode(0)
12        dummy.next = head
13        curr_tail = dummy
14        
15        while True:
16            segment_end = curr_tail
17            for _ in range(k):
18                segment_end = segment_end.next
19                if not segment_end:
20                    return dummy.next
21            
22            next_segment_start = segment_end.next
23        
24            prev = next_segment_start 
25            curr = curr_tail.next
26            for _ in range(k):
27                temp_next = curr.next
28                curr.next = prev
29                prev = curr
30                curr = temp_next
31            
32            new_segment_tail = curr_tail.next
33            curr_tail.next = prev
34            curr_tail = new_segment_tail
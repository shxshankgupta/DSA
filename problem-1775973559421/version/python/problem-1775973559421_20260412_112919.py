# Last updated: 4/12/2026, 11:29:19 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head or not head.next:
9            return head
10        
11        slow, fast = head, head.next
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15        
16        mid = slow.next
17        slow.next = None  
18        
19        left = self.sortList(head)
20        right = self.sortList(mid)
21        
22        return self.merge(left, right)
23    
24    def merge(self, list1, list2):
25        dummy = ListNode()
26        tail = dummy
27        
28        while list1 and list2:
29            if list1.val < list2.val:
30                tail.next = list1
31                list1 = list1.next
32            else:
33                tail.next = list2
34                list2 = list2.next
35            tail = tail.next
36            
37        tail.next = list1 if list1 else list2
38        return dummy.next
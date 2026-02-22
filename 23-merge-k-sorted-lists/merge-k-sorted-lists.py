# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        arr = []
        for l in lists:
            curr_list_node = l
            while curr_list_node:
                arr.append(curr_list_node.val)
                curr_list_node = curr_list_node.next
        
        # 2. Sort the collected values
        arr.sort()
        
        # 3. Create the new linked list (Your existing logic)
        dummy = ListNode(0)
        current = dummy
        for value in arr:
            current.next = ListNode(value)
            current = current.next
            
        return dummy.next
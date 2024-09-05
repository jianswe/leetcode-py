from typing import Optional
from linkedlist.list_node import ListNode

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        # before: before the first node of current group 
        # end: the last node of current group 
        before, end = dummy, dummy 
        while end: 
            for i in range(k):
                end = end.next 
                if not end: 
                    break 
            if not end: 
                break 
            head_of_reverse_group, head_of_next_group = self.reverseKNodes(before.next, k)
            end_of_reverse_group = before.next
            before.next = head_of_reverse_group
            end_of_reverse_group.next = head_of_next_group
            before, end = end_of_reverse_group, end_of_reverse_group
        return dummy.next

    # reverse k nodes start from head 
    # return the head of reversed current group and the head of next group 
    def reverseKNodes(self, head: Optional[ListNode], k: int) -> (Optional[ListNode], Optional[ListNode]): 
        prev, curr, next = None, head, None 
        for i in range(k): 
            next = curr.next 
            curr.next = prev 
            prev, curr = curr, next
        return prev, curr 

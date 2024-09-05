from typing import Optional
from linkedlist.list_node import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, next = None, head, None 
        while curr:
            next = curr.next 
            curr.next = prev 
            prev = curr
            curr = next 
        head = prev 
        return head 
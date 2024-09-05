from typing import Optional
from linkedlist.list_node import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head 
        for i in range(n):
            right = right.next
        if not right:
            return head.next
        while right.next:
            left = left.next 
            right = right.next 
        left.next = left.next.next 
        return head 
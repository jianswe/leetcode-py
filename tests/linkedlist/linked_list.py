from typing import List, Optional
from linkedlist.list_node import ListNode

class LinkedList:
    def __init__(self, nums: List[int]):
        dummy = ListNode()
        cur = dummy
        for num in nums:
            cur.next = ListNode(num)
            cur = cur.next
        self.head = dummy.next

    @staticmethod
    def traverse(head: Optional[ListNode]) -> List[int]:
        ans = []
        cur = head 
        while cur:
            ans.append(cur.val)
            cur = cur.next
        return ans  

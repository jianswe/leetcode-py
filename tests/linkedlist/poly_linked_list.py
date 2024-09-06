from typing import List, Optional
from linkedlist.addPloy import PolyNode

class PolyLinkedList: 
    def __init__(self, cps: List[List[int]]):
        dummy = PolyNode()
        cur = dummy
        for coefficient, power in cps: 
            cur.next = PolyNode(coefficient, power)
            cur = cur.next 
        self.head = dummy.next

    @staticmethod
    def traverse(head: Optional[PolyNode]) -> List[int]:
        ans = []
        cur = head 
        while cur:
            ans.append([cur.coefficient, cur.power])
            cur = cur.next
        return ans  
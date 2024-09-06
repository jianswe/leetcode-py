# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        p1, p2 = poly1, poly2
        dummy = PolyNode()
        p = dummy
        while p1 or p2:
            if not p2: 
                p.next = PolyNode(p1.coefficient, p1.power)
                p = p.next
                p1 = p1.next
            elif not p1: 
                p.next = PolyNode(p2.coefficient, p2.power)
                p = p.next
                p2 = p2.next
            elif p1.power > p2.power:
                p.next = PolyNode(p1.coefficient, p1.power)
                p = p.next
                p1 = p1.next
            elif p1.power < p2.power:
                p.next = PolyNode(p2.coefficient, p2.power)
                p = p.next
                p2 = p2.next
            else: # p1.power == p2.power
                coefficient = p1.coefficient + p2.coefficient
                if coefficient != 0:
                    p.next = PolyNode(coefficient, p1.power)
                    p = p.next 
                p1 = p1.next 
                p2 = p2.next 
        return dummy.next
        
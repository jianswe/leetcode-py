import pytest
from linkedlist.addPloy import Solution
from poly_linked_list import PolyLinkedList

@pytest.mark.parametrize("poly1, poly2, expected", [
    ([[1,1]], [[1,0]], [[1,1],[1,0]]), 
    ([[2,2],[4,1],[3,0]], [[3,2],[-4,1],[-1,0]], [[5,2],[2,0]]), 
    ([[1,2]], [[-1,2]], [])
])
def test_addPoly(poly1, poly2, expected):
    polyList1 = PolyLinkedList(poly1)
    polyList2 = PolyLinkedList(poly2)
    s = Solution()
    newPoly = s.addPoly(polyList1.head, polyList2.head)
    output = PolyLinkedList.traverse(newPoly)
    assert output == expected


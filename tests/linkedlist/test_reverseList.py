from linkedlist.ListNode import ListNode
from linkedlist.reverseList import Solution
from traverseLinkedList import traverseLinkedList

def test_reverseList():
    head = ListNode(1)
    cur = head 
    for i in range(2,6):
        cur.next = ListNode(i)
        cur = cur.next
    output = [5, 4, 3, 2, 1]
    solution = Solution()
    head = solution.reverseList(head)
    ans = traverseLinkedList(head)
    assert ans == output
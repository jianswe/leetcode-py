from linkedlist.ListNode import ListNode
from linkedlist.removeNthFromEnd import Solution
from traverseLinkedList import traverseLinkedList

def test_removeNthFromEnd():
    head = ListNode(1)
    cur = head 
    for i in range(2,6):
        cur.next = ListNode(i)
        cur = cur.next
    output = [1,2,3,5]
    solution = Solution()
    newHead = solution.removeNthFromEnd(head, 2)
    ans = traverseLinkedList(newHead)
    assert ans == output
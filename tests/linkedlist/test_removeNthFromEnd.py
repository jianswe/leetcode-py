from linkedlist.list_node import ListNode
from linkedlist.removeNthFromEnd import Solution
from linked_list import LinkedList

def test_removeNthFromEnd():
    test_cases = [
        ([1,2,3,4,5], 2, [1,2,3,5]),
        ([1], 1, []),
        ([1,2], 1, [1])
    ]
    for nums, n, output in test_cases: 
        linkedList = LinkedList(nums)
        solution = Solution()
        newHead = solution.removeNthFromEnd(linkedList.head, n)
        ans = LinkedList.traverse(newHead)
        assert ans == output
from linkedlist.list_node import ListNode
from linkedlist.reverseList import Solution
from linked_list import LinkedList

def test_reverseList():
    test_cases = [
        ([1,2,3,4,5], [5,4,3,2,1]),
        ([1,2], [2,1]),
        ([], [])
    ]

    for nums, output in test_cases: 
        linkedList = LinkedList(nums)
        solution = Solution()
        head = solution.reverseList(linkedList.head)
        ans = LinkedList.traverse(head)
        assert ans == output
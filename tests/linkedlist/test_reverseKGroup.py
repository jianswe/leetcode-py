from linkedlist.reverseKGroup import Solution
from linked_list import LinkedList

def test_reverseKGroup():
    test_cases = [
        ([1,2,3,4,5], 2, [2,1,4,3,5]), 
        ([1,2,3,4,5], 3, [3,2,1,4,5]), 
    ]
    solution = Solution()
    for nums, k, output in test_cases: 
        linkedList = LinkedList(nums)
        newHead = solution.reverseKGroup(linkedList.head, k)
        assert LinkedList.traverse(newHead) == output
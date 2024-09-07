import pytest
from tree.zigzagLevelOrder import Solution
from binary_tree import BinaryTree

@pytest.mark.parametrize("nums, expected", [
    ([3,9,20,None,None,15,7], [[3],[20,9],[15,7]]), 
    ([1], [[1]]),
    ([], [])
])
def test_zigzagLevelOrder(nums, expected):
    bt = BinaryTree(nums)
    s = Solution()
    assert s.zigzagLevelOrder(bt.root) == expected
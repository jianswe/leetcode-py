import pytest
from tree.levelOrder import Solution
from binary_tree import BinaryTree

@pytest.mark.parametrize("nums, expected", [
    ([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]),
    ([1], [[1]]),
    ([], [])
])
def test_levelOrder(nums, expected):
    bt = BinaryTree(nums)
    s = Solution()
    assert s.levelOrder(bt.root) == expected
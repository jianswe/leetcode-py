import pytest
from tree.tree_node import TreeNode
from tree.diameterOfBinaryTree import Solution
from binary_tree import BinaryTree

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,4,5], 3), 
    ([1,2], 1)
])
def test_diameterOfBinaryTree(nums, expected):
    bt = BinaryTree(nums)
    s = Solution()
    assert s.diameterOfBinaryTree(bt.root) == expected

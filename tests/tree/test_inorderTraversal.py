import pytest
from tree.inorderTraversal import Solution
from binary_tree import BinaryTree

@pytest.mark.parametrize("nums, expected", [
    ([1,None,2,3], [1,3,2]), 
    ([1,2,3,4,5,None,8,None,None,6,7,9], [4,2,6,5,7,1,3,9,8]), 
    ([], []),
    ([1], [1])
])
def test_inorderTraversal(nums, expected):
    s = Solution()
    bt = BinaryTree(nums)
    output = s.inorderTraversal(bt.root)
    assert output == expected
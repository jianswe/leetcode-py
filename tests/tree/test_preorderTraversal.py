import pytest
from tree.preorderTraversal import Solution
from binary_tree import BinaryTree

@pytest.mark.parametrize("nums, expected", [
    ([1,None,2,3], [1,2,3]),
    ([1,2,3,4,5,None,8,None,None,6,7,9], [1,2,4,5,6,7,3,8,9]), 
    ([], []), 
    ([1], [1])
])
def test_preorderTraversal(nums, expected): 
    bt = BinaryTree(nums)
    s = Solution()
    assert s.preorderTraversal(bt.root) == expected
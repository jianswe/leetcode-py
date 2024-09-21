import pytest 
from tree.postorderTraversal import Solution
from binary_tree import BinaryTree

@pytest.mark.parametrize("nums, expected", [
    ([1,None,2,3], [3,2,1]),
    ([1,2,3,4,5,None,8,None,None,6,7,9], [4,6,7,5,2,9,8,3,1]), 
    ([], []), 
    ([1], [1])
])
def test_postorderTraversal(nums, expected): 
    s = Solution()
    bt = BinaryTree(nums)
    assert s.postorderTraversal(bt.root) == expected
import pytest
from tree.flatten import Solution
from binary_tree import BinaryTree

@pytest.mark.parametrize("original, flat", [
    ([1,2,5,3,4,None,6], [1,None,2,None,3,None,4,None,5,None,6]), 
    ([], []),
    ([0], [0])
])
def test_flatten(original, flat):
    bt = BinaryTree(original)
    s = Solution()
    s.flatten(bt.root)
    output = BinaryTree.levelOrderTraversal(bt.root)
    assert output == flat
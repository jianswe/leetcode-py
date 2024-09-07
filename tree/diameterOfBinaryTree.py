from typing import Optional
from tree.tree_node import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node): 
            if not node: 
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            nonlocal diameter
            diameter = max(diameter, leftHeight+rightHeight)
            return max(leftHeight, rightHeight)+1

        diameter = 0
        dfs(root)
        return diameter
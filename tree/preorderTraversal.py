from typing import List, Optional
from tree.tree_node import TreeNode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        ans = [root.val]
        ans += self.preorderTraversal(root.left)
        ans += self.preorderTraversal(root.right)
        return ans 
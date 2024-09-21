from typing import List, Optional
from tree.tree_node import TreeNode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        ans = self.postorderTraversal(root.left)
        ans += self.postorderTraversal(root.right)
        ans += [root.val]
        return ans 
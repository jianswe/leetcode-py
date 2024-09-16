from typing import List, Optional
from tree.tree_node import TreeNode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        ans = []
        ans += self.inorderTraversal(root.left)
        ans.append(root.val) 
        ans += self.inorderTraversal(root.right)
        return ans 
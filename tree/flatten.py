from typing import Optional
from tree.tree_node import TreeNode

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root 
        while cur: 
            if cur.left: 
                last = cur.left 
                while last.right: 
                    last = last.right 
                last.right = cur.right
                cur.right = cur.left 
                cur.left = None 
            cur = cur.right 
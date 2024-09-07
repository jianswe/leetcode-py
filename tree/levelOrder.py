from typing import List, Optional
from tree.tree_node import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        queue, result = [root], []
        while queue: 
            next_queue, ans = [], []
            for node in queue: 
                ans.append(node.val)
                if node.left: 
                    next_queue.append(node.left)
                if node.right: 
                    next_queue.append(node.right)
            result.append(ans)
            queue = next_queue
        return result 
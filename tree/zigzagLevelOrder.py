from collections import deque
from typing import List, Optional
from tree.tree_node import TreeNode

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        dq = deque([root])
        result = []
        reverse = False 
        while dq:
            size = len(dq)
            result.insert(len(result), [])
            for i in range(size): 
                if not reverse: 
                    node = dq.popleft()
                    result[len(result)-1].append(node.val)
                    if node.left: 
                        dq.append(node.left)
                    if node.right: 
                        dq.append(node.right)
                else: 
                    node = dq.pop()
                    result[len(result)-1].append(node.val)
                    if node.right: 
                        dq.appendleft(node.right)
                    if node.left: 
                        dq.appendleft(node.left)
            reverse = not reverse 
        return result 
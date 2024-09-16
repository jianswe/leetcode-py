from typing import Optional
from graph.node import Node

class Solution:
    def __init__(self):
        self.cloned = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        new_node = Node(node.val)
        self.cloned[node] = new_node
        for nei in node.neighbors: 
            if nei not in self.cloned: 
                self.cloneGraph(nei)
            new_node.neighbors.append(self.cloned[nei])
        return new_node

from typing import List, Optional
from collections import defaultdict
from graph.node import Node

class ConnectedGraph: 

    def __init__(self, adjList: List[List[int]]):
        self.size = len(adjList)
        self.nodes = [Node(i+1) for i in range(self.size)]
        for i in range(self.size): 
            for adj in adjList[i]: 
                self.nodes[i].neighbors.append(self.nodes[adj-1])
        self.root = self.nodes[0] if self.nodes else None

    def traverse(self, root: Optional['Node']) -> List[List[int]]:
        adjList = [[] for i in range(self.size)]

        def recursion(node): 
            for nei in node.neighbors: 
                adjList[node.val-1].append(nei.val)
                if not adjList[nei.val-1]: 
                    recursion(nei)

        if root: 
            recursion(root)
        return adjList
            

        
        
import pytest 
from graph.cloneGraph import Solution
from connected_graph import ConnectedGraph

@pytest.mark.parametrize("adjList", [
    ([[2,4],[1,3],[2,4],[1,3]]),
    ([[]]),
    ([])
])
def test_cloneGraph(adjList):
    graph = ConnectedGraph(adjList)
    s = Solution()
    new_root = s.cloneGraph(graph.root)
    output = graph.traverse(new_root)
    assert output == adjList
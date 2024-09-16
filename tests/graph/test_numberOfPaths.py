import pytest
from graph.numberOfPaths import Solution

@pytest.mark.parametrize("n, corridors, expected", [
    (5, [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]], 2),
    (4, [[1,2],[3,4]], 0)
])
def test_numberOfPaths(n, corridors, expected): 
    s = Solution()
    assert s.numberOfPaths(n, corridors) == expected
import pytest
from graph.networkDelayTime import Solution

@pytest.mark.parametrize("times, n, k, expected", [
    ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
    ([[1,2,1]], 2, 1, 1), 
    ([[1,2,1]], 2, 2, -1)
])
def test_networkDelayTime(times, n, k, expected):
    s = Solution()
    assert s.networkDelayTime(times, n, k) == expected
    
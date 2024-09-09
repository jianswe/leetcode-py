import pytest
from heap.minStoneSum import Solution

@pytest.mark.parametrize("piles, k, expected", [
    ([5,4,9], 2, 12),
    ([4,3,6,7], 3, 12)
])
def test_minStoneSum(piles, k, expected):
    s = Solution()
    assert s.minStoneSum(piles, k) == expected
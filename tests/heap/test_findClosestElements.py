import pytest 
from heap.findClosestElements import Solution

@pytest.mark.parametrize("arr, k, x, expected", [
    ([1,2,3,4,5], 4, 3, [1,2,3,4]),
    ([1,2,3,4,5], 4, -1, [1,2,3,4])
])
def test_findClosestElements(arr, k, x, expected):
    s = Solution()
    assert s.findClosestElements(arr, k, x) == expected
from heap.kthSmallest import Solution

def test_kthSmallest():
    test_cases = [
        ([[1,5,9],[10,11,13],[12,13,15]], 8, 13),
        ([[-5]], 1, -5)
    ]
    s = Solution()
    for matrix, k, output in test_cases: 
        assert s.kthSmallest(matrix, k) == output
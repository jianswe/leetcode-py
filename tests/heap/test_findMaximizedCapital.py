from heap.findMaximizedCapital import Solution 

def test_findMaximizedCapital():
    test_cases = [
        (2, 0, [1,2,3], [0,1,1], 4), 
        (3, 0, [1,2,3], [0,1,2], 6)
    ]
    s = Solution()
    for k, w, profits, capital, output in test_cases: 
        assert s.findMaximizedCapital(k, w, profits, capital) == output
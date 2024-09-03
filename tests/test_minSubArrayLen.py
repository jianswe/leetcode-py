from src.minSubArrayLen import Solution

def test_minSubArrayLen():
    test_cases = [
        (7, [2,3,1,2,4,3], 2),
        (4, [1,4,4], 1),
        (11, [1,1,1,1,1,1,1,1], 0)
    ]
    solution = Solution()
    for target, nums, output in test_cases: 
        assert solution.minSubArrayLen(target, nums) == output

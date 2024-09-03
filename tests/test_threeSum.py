from src.threeSum import Solution

def test_threeSum(): 
    test_cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]])
    ]
    solution = Solution()
    for nums, output in test_cases:
        ans = solution.threeSum(nums) 
        ansSet = set([tuple(triple) for triple in ans])
        outputSet = set([tuple(triple) for triple in output])
        assert ansSet == outputSet
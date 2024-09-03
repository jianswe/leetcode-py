from src.moveZeroes import moveZeroes

def test_moveZeroes():
    test_cases = [
        ([0,1,0,3,12], [1,3,12,0,0]), 
        ([0], [0])
    ]
    for nums, output in test_cases: 
        moveZeroes(nums)
        for i in range(len(output)):
            assert nums[i] == output[i]
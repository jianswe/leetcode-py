from src.moveZeroes import moveZeroes

def test_moveZeroes():
    nums = [0,1,0,3,12]
    output = [1,3,12,0,0]
    moveZeroes(nums)
    for i in range(len(output)):
        assert nums[i] == output[i]
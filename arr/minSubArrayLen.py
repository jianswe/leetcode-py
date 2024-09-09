from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j, sum, ans = 0, 0, 0, float('inf') 
        while j<len(nums):
            while j<len(nums) and sum<target:
                sum+=nums[j]
                j+=1
            # print(i,j)
            if j==len(nums) and sum<target and ans == float('inf'):
                return 0
            while sum>=target: 
                sum-=nums[i]
                i+=1
            ans = min(ans, j-i+1)
        return ans 
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k] < 0: 
                    j+=1
                else: 
                    k-=1 
        return [list(triple) for triple in ans]
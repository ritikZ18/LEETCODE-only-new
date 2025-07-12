# Last updated: 7/11/2025, 7:12:43 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        element = []
        for i in range(0,n) : 
            for  j in range(i+1,n):
                if(nums[i] + nums[j] == target) : 
                    return i,j
        
        return element[i,j]
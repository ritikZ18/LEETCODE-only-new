# Last updated: 7/11/2025, 7:11:47 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = {} #init empty dict 
        for i in range(len(nums)):
            if nums[i] in diff : 
                return [diff[nums[i]], i]
                
            diff[ target - nums[i]] = i 
        return []


        
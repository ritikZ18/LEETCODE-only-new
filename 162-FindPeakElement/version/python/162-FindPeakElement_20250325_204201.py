# Last updated: 3/25/2025, 8:42:01 PM
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0 
        right = len(nums) - 1

        while left < right : 
            mid = (left + right ) // 2

            if nums[mid] <= nums[mid+1] :
                left = mid + 1
            elif nums[mid] > nums[mid+1] : 
                right = mid 
            
            elif left == right : 
                return left
        
        return left 
        
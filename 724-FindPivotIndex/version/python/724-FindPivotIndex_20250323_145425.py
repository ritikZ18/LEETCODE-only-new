# Last updated: 3/23/2025, 2:54:25 PM
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sumLeft = 0 
        # for irtem : in nums : 
        # sumRight += items
        sumRight = sum(nums)

        # go throught the arr, 
        
        for i in range(len(nums)) : 
            sumRight -= nums[i]     #for first element 

            if sumLeft == sumRight :
                return i 
            sumLeft += nums[i]      # else addup to leftSum

        

        

        return -1
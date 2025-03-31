# Last updated: 3/31/2025, 11:51:56 AM
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        first = float('inf')
        second = float('inf')

   
        for num in nums : 
            if num <= first : 
                first = num
            
            elif num <= second : 
                second = num 
            
            else : 
                return True 
        
        return False 
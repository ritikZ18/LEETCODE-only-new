class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        #  logic is simple the visited are marked as negativee
        for num in nums : 
                num = abs(num)
                if nums[num-1] < 0 : 
                    result.append(num)
                else : 
                    nums[num-1] *= -1
        return result 

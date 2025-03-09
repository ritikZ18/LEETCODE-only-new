class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # implement set for eliminate the duplicate in the list 
        # then create empty array to store the results 
        # iterate from 1 to len + 1  coz ( duplicates) & len factor 
        # append in the resukt not present elements 

        nums_sets = set(nums)
        result = []

        for i in range(1, len(nums) + 1) : 
            if i not in nums_sets : 
                result.append(i)
        return result
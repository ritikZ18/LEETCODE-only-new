class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap=set()
        duplicte=[]
        for ele in nums:
            if ele in hashmap:
                duplicte.append(ele)
                continue
            hashmap.add(ele)
        return duplicte

        
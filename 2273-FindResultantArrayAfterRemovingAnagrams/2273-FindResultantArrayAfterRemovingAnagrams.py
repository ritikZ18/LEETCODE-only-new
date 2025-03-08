class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result=[]
        prev=None
        for i in words:
            sort=''.join(sorted(i))
            if prev!=sort:
                result.append(i)
                prev=sort
        return result



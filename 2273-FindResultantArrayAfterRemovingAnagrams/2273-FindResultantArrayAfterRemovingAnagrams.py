class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        group = defaultdict(list)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        result = []
        prev_key = None  #tracks prev sstored string

        for s in words : 
            count = [0] * 26

            for char in s : 
                #get the index of the matched letter
                index = letters.index(char)
                count[index] += 1
            key = tuple(count)       # the char  with all 0 , 1  , create tupled key
           

        
            #  only add if not consective anagram 
            if key != prev_key : 
                result.append(s)
        
            prev_key = key      # update for prev_key with key, for iteration

        return result 
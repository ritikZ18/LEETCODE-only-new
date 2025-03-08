class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        group = defaultdict(list)       #imported
        letters = 'abcdefghijklmnopqrstuvwxyz'

        for s in strs : 
            count = [0] * 26    # [ a:0,0,0,.....,z:0]

            for char in s : 
                index = letters.index(char)     
                count[index] +=1 

            key = tuple(count)      # for cat : count -->  ( a1, 0 , c:1 , 0,0,0,0.....t:1,...z:0)  alphabets redundant
            group[key].append(s)    # here they will group with key (#cat). will append with str only same

        return list(group.values())     #
            
            
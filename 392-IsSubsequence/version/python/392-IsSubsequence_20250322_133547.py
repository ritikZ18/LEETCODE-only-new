// Last updated: 3/22/2025, 1:35:47 PM
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_pointer = 0 
        t_pointer = 0 

        while s_pointer < len(s) and t_pointer < len(t) : 
            if s[s_pointer] == t[t_pointer] : 
                s_pointer += 1 
            
            t_pointer += 1
        
        return s_pointer == len(s)



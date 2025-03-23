# Last updated: 3/23/2025, 3:09:19 PM
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = []

        summ = 0
        alt.append(summ)
        for i in range(len(gain)) :
            summ += gain[i]
            alt.append(summ)

        maxAlt = 0 
        for i in range(len(alt)) : 
 
            if alt[i] > maxAlt : 
                maxAlt =  alt[i]
        
        return maxAlt



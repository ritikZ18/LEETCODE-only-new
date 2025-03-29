# Last updated: 3/28/2025, 5:28:57 PM
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [0]*n
        counter = 0 

        for i in range(n) : 
            if visited[i] == 0 : 
                self.isVisited(isConnected, visited, i)
                counter+=1 
    
        return counter 
            




        # using the recursive we have to check is visited, & connected

    def isVisited(self, isConnected, visited, i ) : 
          n = len(isConnected)
          for k in range(n) : 
            if isConnected[i][k] == 1 and visited[k] == 0 : 
                visited[k] = 1
                self.isVisited(isConnected, visited, k)
        

# Last updated: 3/28/2025, 1:02:28 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        # same as the depth of the tree , left --> right [ taking first element from queue ]

        if not root : 
            return [] 

        q = deque([root])       # created double ended Q on root
        result = []             # to store the output 

        while q : 
            right_val = None 

            for _ in range(len(q)) : 
                # [ 1 , 2  , 3, null, 5, nill, 4 ]   need first popleft ( from collections) 

                right_val = q.popleft()

                # for left first then right
                if right_val.left :
                    q.append(right_val.left)

                # for right check going
                if right_val.right : 
                    q.append(right_val.right)
           
            result.append(right_val.val)        # after the loop... for every val in root, wee need append

        return result  

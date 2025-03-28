# Last updated: 3/28/2025, 2:22:28 PM
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        que=deque([root])
        max_sum=float('-inf')
        max_level=1
        level=0
        while que:
            level+=1
            n=len(que)
            curr_sum=0
            for i in range(n):
                node=que.popleft()
                curr_sum+=node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if curr_sum>max_sum:
                max_sum=curr_sum
                max_level=level
        return max_level
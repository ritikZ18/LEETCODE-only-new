// Last updated: 3/21/2025, 3:03:51 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        max_sum = 0                 # init max_Sum
        slow, fast = head, head         # init the two pointer mech

        while fast and fast.next != None : 
            slow = slow.next 
            fast = fast.next.next       # reach the relative centre of the linkedList 

# new pointer's for break the LinkedList , in two

        current = slow                  # init the pointer, at slow, to make it break point
        prev = None                     # this will be the new end point of LL

        while current : 
            temp = current.next             # temp to store last element of the LL
            current.next = prev             # broked the LL and pointed  last LL element to prev : NONE 
            prev = current                  # swap the elements 
            current = temp                  # swap the elements [ ]
        
        head2 = prev                        # new head of new LL 


        while head2:
            max_sum = max(max_sum, head.val + head2.val)
            head = head.next                # update to next position of head
            head2 = head2.next 
        return max_sum


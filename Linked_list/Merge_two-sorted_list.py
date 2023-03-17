"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        #tail of sorted list is dummy for now
        tail = dummy
        while(list1 and list2):
            if(list1.val < list2.val):
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next
            #update the tail next
            tail = tail.next
        #the while loop ends once one of the list is exhausted
        #if list1 is still left append that to tail
        if list1:
                tail.next = list1
        else:
                tail.next = list2
        #dummy stores the sorted list and pass the next value to give entire list
        #initial dummy is empty
        return dummy.next
      
      
      
      
      
      

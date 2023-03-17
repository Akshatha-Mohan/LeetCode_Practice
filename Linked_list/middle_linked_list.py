"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        start = node = head
        while start:
            length = length + 1
            start = start.next
        middle = length//2
        counter = 0
        while node:
            if(counter == middle):
                return node
            else:
                counter+=1
                node = node.next
        return None
      
      
      
      
      
      


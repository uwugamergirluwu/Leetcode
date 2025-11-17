# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        countPointer = head
        midPointer = head
        count=0
        while countPointer:
            countPointer = countPointer.next
            count+=1
        count = math.ceil(count/2)
        while count>0:
            midPointer = midPointer.next
            count-=1
        return midPointer
        
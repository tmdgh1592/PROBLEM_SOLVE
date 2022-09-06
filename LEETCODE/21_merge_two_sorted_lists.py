# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        my_list = []

        while l1 or l2:
            if l1:
                my_list.append(l1.val)
                l1 = l1.next
            else:
                my_list.append(l2.val)
                l2 = l2.next

        my_list.sort()

        mergedList = head = None

        for val in my_list:
            if not mergedList:
                mergedList = ListNode(val)
                head = mergedList
            else:
                mergedList.next = ListNode(val)
                mergedList = mergedList.next

        return head
            
            


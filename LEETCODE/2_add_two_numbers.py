# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def toList(self, node: ListNode) -> list:
        my_list = []

        while node:
            my_list.append(node.val)
            node = node.next

        return my_list
            
    def toReversedLinkedList(self, result:str) -> ListNode:
        prev: ListNode = None

        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reversedList1 = self.toList(self.reverseList(l1))
        reversedList2 = self.toList(self.reverseList(l2))

        num1 = ''.join(str(e) for e in reversedList1)
        num2 = ''.join(str(e) for e in reversedList2)

        return self.toReversedLinkedList(str(int(num1) + int(num2)))
import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        root = ListNode(None)

        for lst in lists:
            node = lst
            while node:
                heapq.heappush(q, node.val)
                node = node.next


        cur = root
        while q:
            val = heapq.heappop(q)
            node = ListNode(val)

            cur.next = node
            cur = cur.next

        return root.next
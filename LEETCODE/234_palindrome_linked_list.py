# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque
from typing import Optional

# 리스트로 변환하여 풀ㅣ
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        q = deque()

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True
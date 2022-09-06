# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque
from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # fast가 None이 아니면 홀수개의 입력임.
        if fast:
            slow = slow.next #중앙값은 팰린드롬 고려에서 제외하기 위해 한 칸 더 이동

        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        
        return not rev



# 리스트로 변환하여 풀이
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         if not head:
#             return True

#         q = deque()

#         node = head

#         while node is not None:
#             q.append(node.val)
#             node = node.next

        
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
        
#         return True
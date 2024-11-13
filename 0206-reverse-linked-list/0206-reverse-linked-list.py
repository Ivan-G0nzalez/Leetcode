# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None # Node 3-> 2 -> 1
        
        while current:
            next = current.next # 4 -> 5 -> None
            current.next = prev # 3 -> 2 -> 1 -> None
            prev = current # 4 -> 5
            current = next # 3 -> 4 -> 5 -> None
        
        return prev
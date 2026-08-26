# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        res = self.reverseList(head.next)
        if res == None:
            return head
        else: 
            head.next.next = head
            head.next = None
        return res
        
        
        
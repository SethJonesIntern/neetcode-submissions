# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 1
        while(temp.next is not None):
            temp = temp.next
            count += 1
        if count == 1 or count == n:
            return head.next
        temp = head
        for i in range(count - n - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head

       
        
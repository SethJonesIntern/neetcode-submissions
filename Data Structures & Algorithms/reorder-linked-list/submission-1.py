# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if(not head or not head.next):
            return

        # Get length
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        # Go to node n/2 - 1, add 1 for odd length
        temp = head
        for i in range(count // 2 - 1):
            temp = temp.next
        if count % 2 == 1:
            temp = temp.next

        # cut the list
        temp2 = temp.next
        temp.next = None
        temp = temp2

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None:
                return None
            res = reverseList(head.next)
            if res == None:
                return head
            else:
                head.next.next = head
                head.next = None
            return res

        temp = reverseList(temp)
        # weird crisscross
        while head and temp:
            headnext = head.next
            head.next = temp

            tempnext = temp.next
            temp.next = headnext

            head = headnext
            temp = tempnext

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        smap = defaultdict(list)
        while(head != None):
            if head.val in smap:
                if head in smap[head.val]:
                    return True
            if head.next == None:
                return False
            smap[head.val].append(head)
            head = head.next
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        while list1 and list2:    
            if res == None:
                if(list1.val < list2.val):
                    res = list1
                    list1 = list1.next
                else:
                    res = list2
                    list2 = list2.next
                beg = res
                continue
            if(list1.val < list2.val):
                    res.next = list1
                    res = res.next
                    list1 = list1.next
            else:
                res.next = list2
                res = res.next
                list2 = list2.next
        if(list1):
            if(res):
                res.next = list1
            else: 
                res = list1
                beg = res 
        else:
            if(res):
                res.next = list2
            else: 
                res = list2
                beg = res
        
        return beg

    
        
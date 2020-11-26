class Solution(object):
    def mergeTwoLists(self, l1, l2):
        result = current = ListNode(0) 
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next= l1
                l1= l1.next
            else:
                current.next= l2
                l2= l2.next
            current= current.next
        
        if l1 is not None:
            current.next = l1
        elif l2 is not None:
            current.next = l2
        
        return result.next

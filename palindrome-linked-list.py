# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        temp = head
​
        while(temp): # while(temp)
            res.append(temp.val) # res.append(temp.val)
            temp = temp.next # temp = temp.val
          
        while(len(res)//2 != 0): # while(len(res)):
            if head.val != res.pop():
                return False
            head = head.next
        return True
    
    
    
    
    
        
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         print(head)
#         if head is None:
#             return True
#         result=[]
#         temp=head
        
        
#         while(temp != None):
#             print(temp.val)

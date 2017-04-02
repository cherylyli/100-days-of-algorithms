# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        # init output node
        output = ListNode((l1.val + l2.val)%10)
        output_node = output
        carry = (l1.val + l2.val)//10

        l1 = l1.next
        l2 = l2.next
        
        
        
        # keep adding digits
        while l1 and l2:
            
            sum = l1.val + l2.val + carry
            output.next = ListNode(sum%10)
            carry = sum//10
            
            l1 = l1.next
            l2 = l2.next 
            output = output.next
            
        # keep adding l1 nodes if l1 has more nodes
        while l1:
            sum = l1.val + carry
            output.next = ListNode(sum%10)
            carry = sum//10
            l1 = l1.next
            output = output.next
       
       # keep adding l2 nodes if l2 has more nodes
        while l2:
            sum = l2.val + carry
            output.next = ListNode(sum%10)
            carry = sum//10
            l2 = l2.next 
            output = output.next
            
        # add carry if larger than 0
        if carry > 0:
            output.next = ListNode(carry)
            
        return output_node
        
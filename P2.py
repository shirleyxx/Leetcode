# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = l1.val+l2.val
        carry = curr//10
        curr = curr % 10
        head = ListNode(curr)
        p = head
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            curr = l1.val + l2.val + carry
            carry = curr//10
            curr = curr % 10
            p.next = ListNode(curr)
            p = p.next
        
        if l2.next:
            l1 = l2
            
        while l1.next:
            l1 = l1.next
            curr = carry + l1.val
            carry = curr//10
            curr = curr % 10
            p.next = ListNode(curr)
            p = p.next
            
        if carry != 0:
            p.next = ListNode(carry)
            
        return head

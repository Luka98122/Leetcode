# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        res = 0
        power = 0
        
        if not l1.next:
            res+=l1.val
        if not l2.next:
            res += l2.val

        while l1.next or l2.next:
            if l1.next:
                res+=l1.val*(10**power)
                l1 = l1.next
                if l1.next==None:
                    res+=l1.val*(10**(power+1))
            if l2.next:
                res+=l2.val*(10**power)
                l2 = l2.next
                if l2.next==None:
                    res+=l2.val*(10**(power+1))
            power+=1
        
        rootNode = ListNode()
        curNode = rootNode
        x = res
        while x>9:
            cif = x%10
            x = x//10
            curNode.val = cif
            curNode.next = ListNode()
            curNode = curNode.next
        curNode.val = x
        return rootNode
            
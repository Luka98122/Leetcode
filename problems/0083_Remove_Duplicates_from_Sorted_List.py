# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        if not head:
            return head
        while True:
            if not head:
                break
            if head.next:
                if head.next.val == head.val:
                    head.next = head.next.next
                else:
                    head = head.next
            else:
                break
        return dummy.next


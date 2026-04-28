# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next == None: return None

        cur = ListNode(-1,head)
        dummy = ListNode(-1,cur)
        far = head

        for i in range(n):
            far=far.next
        
        while True:
            if far == None:
                cur.next = cur.next.next
                break
            else:
                cur = cur.next
                far = far.next
        
        return dummy.next.next
    
c = Solution()
c.removeNthFromEnd(ListNode(1,ListNode(2)),2)
        
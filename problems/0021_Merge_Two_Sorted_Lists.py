
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        res = ListNode(-1)
        dummy.next = res
        if list1 == None: return list2
        if list2 == None: return list1
        while True:
            if list1==None:
                while list2:
                    res.next = list2
                    res = res.next
                    list2 = list2.next
                break
            if list2==None:
                while list1:
                    res.next = list1
                    res = res.next
                    list1 = list1.next
                break

            if list1.val <= list2.val:
                res.next = list1
                res = res.next
                list1 = list1.next
            else:
                res.next = list2
                res = res.next
                list2 = list2.next
        return dummy.next.next

c = Solution()
c.mergeTwoLists()
        
        
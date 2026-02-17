class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l_stuff = []
        
        while head:
            l_stuff.append(head.val)
            head = head.next
        n = len(l_stuff)
        for i in range(n//2+1):
            if l_stuff[i] != l_stuff[n-1-i]:
                return False
        return True

c = Solution()
print(c.isPalindrome())
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(char for char in s if char.isalnum())
        a = a.lower()
        for i in range(len(a)//2):
            if a[i]!=a[len(a)-1-i]:
                return False
        
        return True

c = Solution()
print(c.isPalindrome("A man, a plan, a canal: Panama"))
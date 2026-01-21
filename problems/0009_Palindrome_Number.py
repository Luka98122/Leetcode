class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        digits = []
        while x>9:
            digits.append(x%10)
            x//=10
        digits.append(x)
        n = len(digits)
        for i in range(n//2):
            if digits[i] != digits[n-1-i]:
                return False
        return True

c = Solution()
print(c.isPalindrome(121))


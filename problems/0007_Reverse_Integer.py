class Solution:
    def reverse(self, x: int) -> int:
        mul = 1
        
        if x<0:
            mul = -1
        digits = []
        x = abs(x)
        cnt = 0
        while x>0:
            dig = x%10
            x//=10
            cnt+=1
            digits.append(dig)
        new_x = 0
        for i,dig in enumerate(digits):
            if new_x+dig*10**(cnt-i-1) < 2**31 -1:
                new_x =  new_x+dig*10**(cnt-i-1)
            else:
                return 0
        new_x*=mul
        return new_x
    

c = Solution()
print(c.reverse(120))
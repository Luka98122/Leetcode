class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        while len(num1) < len(num2):
            num1 = "0"+num1
        
        while len(num2) < len(num1):
            num2 = "0"+num2
        
        a = num1[::-1]
        b = num2[::-1]

        res = ""
        carry = 0
        for i in range(len(num1)):
            s = int(a[i])+int(b[i]) + carry
            carry = s//10
            res+=str(s%10)
        if carry!=0: res+=str(carry)
        res = res[::-1]
        return res
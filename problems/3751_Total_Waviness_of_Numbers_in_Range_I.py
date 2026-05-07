class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for num in range(num1,num2+1):
            if num<100: continue
            s = str(num)
            for i in range(1,len(str(num))-1):
                l = int(s[i-1])
                r = int(s[i+1])
                c = int(s[i])
                if l<c and r<c: res+=1
                if c<l and c<r: res+=1
        return res
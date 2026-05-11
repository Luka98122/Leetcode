class Solution:
    def totalWavinessDP(self, num1: int, num2: int) -> int:
        wavineses = [0]*100001
        for i in range(100,100001):
            r = i%10
            rem = i//10
            c = rem%10
            l = (rem//10)%10
            wave = 0
            
            if (c<l and c<r): wave=1
            if (c>l and c>r): wave=1
            
            wavineses[i] = wave+wavineses[rem]
        
        for i in range(1,100001):
            wavineses[i] += wavineses[i-1]
        
        return wavineses[num2]-wavineses[num1-1]
    
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

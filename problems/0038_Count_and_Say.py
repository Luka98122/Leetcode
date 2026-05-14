class Solution:
    def rle(self,s : str) -> str:
        if len(s)==1: return "1"+s
        res = ""
        cnt = 0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cnt+=1
            else:
                if cnt==0:
                    res+="1"+s[i-1]
                else:
                    res+=str(cnt+1)+s[i-1]
                    cnt = 0
        res+=str(cnt+1)+s[-1]

        return res
    
    def countAndSay(self, n: int) -> str:
        if n==1: return "1"
        return self.rle(self.countAndSay(n-1))

c = Solution()
print(c.rle("1"))
print(c.rle("11"))
print(c.rle("21"))
print(c.rle("3332122"))

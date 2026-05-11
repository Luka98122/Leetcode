class Solution:
    def minOperations(self, s: str) -> int:
        
        """
        I have reached the flow state where I get an idea,
        and as I am typing it I would struggle to explain it,
        but I know why I am doing it, and it works first try.
        """
        a = 0
        b = 0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=="0":
                    a+=1
                else:
                    b+=1
            else:
                if s[i]=="0":
                    b+=1
                else:
                    a+=1
        
        return min(a,b)
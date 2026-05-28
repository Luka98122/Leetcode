class Solution:
    def reformat(self, s: str) -> str:
        let = []
        num = []
        for c in s:
            if c in "0123456789":
                num.append(c)
            else:
                let.append(c)
        
        if abs(len(let)-len(num))<=1:
            res = ""
            for i in range(min(len(num),len(let))):
                res+=num[i]
                res+=let[i]
            
            if len(num) < len(let):
                res = let[len(let)-1]+res
            elif len(let) < len(num):
                res = res + num[len(num)-1]
            return res
        return ""
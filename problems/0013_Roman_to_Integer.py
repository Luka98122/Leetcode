class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        if "IV" in s:
            res+=4
            s = s.replace("IV","")
        if "IX" in s:
            res+=9
            s = s.replace("IX","")
        if "XL" in s:
            res+=40
            s = s.replace("XL","")
        if "XC" in s:
            res+=90
            s = s.replace("XC","")
        if "CD" in s:
            res+=400
            s = s.replace("CD","")
        if "CM" in s:
            res+=900
            s = s.replace("CM","")
        
        vals = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        for k in vals.keys():
            res+=s.count(k)*vals[k]
        return res

c = Solution()
print(c.romanToInt("XIV"))
        
class Solution:
    def intToRoman(self, num: int) -> str:
        a = {
            1 : "I",
            2 : "II",
            3 : "III",
            4 : "IV",
            5 : "V",
            6 : "VI",
            7 : "VII",
            8 : "VIII",
            9 : "IX",
            0 : "",
        }
        b = {
            1 : "X",
            2 : "XX",
            3 : "XXX",
            4 : "XL",
            5 : "L",
            6 : "LX",
            7 : "LXX",
            8 : "LXXX",
            9 : "XC",
            0 : "",
        }
        c = {
            1 : "C",
            2 : "CC",
            3 : "CCC",
            4 : "CD",
            5 : "D",
            6 : "DC",
            7 : "DCC",
            8 : "DCCC",
            9 : "CM",
            0 : "",
        }
        d = {
            1 : "M",
            2 : "MM",
            3 : "MMM",
        }
        abcd = [d,c,b,a]
        res = ""
        digit = 0
        for i in range(4-len(str(num)),4):
            res+=abcd[i][int(str(num)[digit])]
            digit+=1
        return res
        
c = Solution()
print(c.intToRoman(58))
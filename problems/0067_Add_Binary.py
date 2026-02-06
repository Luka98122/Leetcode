class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_sum = 0
        b_sum = 0

        for i in range(len(a)):
            if a[i] == "1":
                a_sum += 2 ** (len(a) - 1 - i)

        for i in range(len(b)):
            if b[i] == "1":
                b_sum += 2 ** (len(b) - 1 - i)

        s = a_sum + b_sum

        if s == 0:
            return "0"

        res = ""
        while s > 0:
            res = str(s % 2) + res
            s //= 2

        return res


c = Solution()
print(c.addBinary("1010","1011"))
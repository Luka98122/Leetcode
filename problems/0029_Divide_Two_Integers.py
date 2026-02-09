class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Handle overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        a = abs(dividend)
        b = abs(divisor)
        result = 0
        # >> bitwise right-shift , effectively int division by a power of two
        for i in range(31, -1, -1):
            if (a >> i) >= b:
                result += 1 << i
                a -= b << i

        return result if sign > 0 else -result

c = Solution()
print(c.divide(7,-3))
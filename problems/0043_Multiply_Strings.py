class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = [0] * (len(num1) + len(num2) - 1)

        for i in range(len(num1)):
            for j in range(len(num2)):
                ans[i + j] += int(num1[i]) * int(num2[j])

        for i in range(len(ans) - 1, 0, -1):
            ans[i - 1] += ans[i] // 10
            ans[i] %= 10

        return "".join(map(str, ans))
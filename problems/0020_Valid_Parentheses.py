class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ["(", "{", "["]
        closes = [")", "}", "]"]
        if len(s)==1:
            return False
        closed = 0
        try:
            for i in range(len(s)):
                stack.append(s[i])
                if stack[-1] in opens:
                    continue
                elif stack[-1] in closes:
                    if opens.index(stack[-2]) == closes.index(stack[-1]):
                        stack.pop()
                        stack.pop()
                        closed+=2
                        continue
                    else:
                        return False
        except: 
            return False
        if closed!=len(s): return False
        return True


c = Solution()
print(c.isValid("(()"))
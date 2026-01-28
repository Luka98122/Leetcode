class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack):
            mismatch = False
            for j in range(len(needle)):
                if (j+i)>=len(haystack): 
                    return -1
                if haystack[i+j]!=needle[j]: 
                    mismatch = True
                    break
            if mismatch==False:
                return i
            i+=1
        return -1

c = Solution()
print(c.strStr("leetcode", "cod"))
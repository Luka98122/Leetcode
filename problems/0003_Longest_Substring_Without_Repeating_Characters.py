class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s =="" or s is None:
            return 0
        l = 0
        r = 1
        cur = {}
        n = len(s)
        best = -1
        bst = ""
        cur[s[l]] = 1
        while r<n:
            if s[r] not in cur.keys():
                cur[s[r]] = 1
                r+=1
            else:
                if best<r-l:
                    best = r-l
                    bst = s[l:r+1]
                del cur[s[l]]
                l+=1
        best = max(best,r-l)
        return best

c = Solution()
print(c.lengthOfLongestSubstring("abcddef"))



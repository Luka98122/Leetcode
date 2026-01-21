class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        best = ""
        shortest = 201
        short_index = 0
        for i,s in enumerate(strs):
            if len(s)<shortest:
                shortest = len(s)
                short_index = i
        for i in range(shortest):
            a = strs[short_index][i]
            br = False
            for st in strs:
                if st[i]!=a:
                    br = True
                    break
            if not br:
                best+=a
            else:
                break
        return best
    
c = Solution()
print(c.longestCommonPrefix(["flower","flow","flight"]))
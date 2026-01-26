class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""]*numRows
        curOffset = 1
        ind = -1
        i = 0
        j = 0
        while j < len(s):
            char = s[j]
            if (i//numRows)%2==0:
                rows[i%numRows]+=char
                ind=-1
            else:
                if ind ==0:
                    i+=2
                    continue
                ind = numRows-1-((i+1)%numRows)
                
                rows[ind] += char
            i+=1
            j+=1
        return "".join(rows)

c = Solution()
print(c.convert("PAYPALISHIRING",4))
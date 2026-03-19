class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if (numRows==0): return []
        if (numRows==1): return [[1]]
        if (numRows==2): return [[1],[1,1]]

        rows = [[1],[1,1]]

        for i in range(0,numRows-2):
            row = [1]
            for j in range(i+1):
                row.append(rows[-1][j]+rows[-1][j+1])
            row.append(1)
            rows.append(row)
            print(row)       

        return rows
    
c = Solution()
print(c.generate(5))
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        x = 0
        y = 0
        h = len(matrix)
        w = len(matrix[0])
        seen = []
        for i in range(len(matrix)):
            seen.append([])
            for j in range(len(matrix[0])):
                seen[-1].append(0)
        seen[0][0] = 1
        # X,Y
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        cd = 0
        res = [matrix[0][0]]
        times = 0
        while True:
            x1 = x+dirs[cd][0]
            y1 = y+dirs[cd][1]

            if x1<w and y1<h and x1>=0 and y1>=0:

                if seen[y1][x1]==0:
                    x = x+dirs[cd][0]
                    y = y+dirs[cd][1]
                    seen[y][x] = 1
                    res.append(matrix[y][x])
                    times = 0
                else:
                    cd+=1
                    cd = cd%4
                    times+=1
            else:
                cd+=1
                cd = cd%4
                times+=1
            
            if times>4:
                break
        return res
    
c = Solution()

print(c.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
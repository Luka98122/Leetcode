class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        maxArea = 0.0
        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    area = abs(
                        x1*(y2 - y3) +
                        x2*(y3 - y1) +
                        x3*(y1 - y2)
                    ) / 2

                    maxArea = max(maxArea, area)

        return maxArea


c = Solution()
print(c.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))

                    
            
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        best = -1
        while l<r:
            cur = min(height[l],height[r]) * (r-l)
            if cur >= best:
                best = cur
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return best


c = Solution()
print(c.maxArea([1,2,1]))
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        if not matrix: return None
        
        res = [0]*len(matrix)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[i]+=matrix[i][j]
        
        return res
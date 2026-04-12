from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cols = []
        rows = []
        
        for row in mat:
            cnt = 0
            for item in row:
                if item==1:
                    cnt+=1
            rows.append(cnt)
        
        for i in range(len(mat[0])):
            cnt = 0
            for j in range(len(mat)):
                if mat[j][i]==1:
                    cnt+=1
            cols.append(cnt)
        
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and rows[i]==1 and cols[j]==1:
                    res +=1
                    
        return res
from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        MOD = 12345
        
        res = [[0] * m for _ in range(n)]
        
        prefix = 1
        for i in range(n):
            for j in range(m):
                res[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD
        
        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                res[i][j] = (res[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD
                
        return res


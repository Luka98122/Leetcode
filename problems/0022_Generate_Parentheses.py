import copy
class Solution:
    def recurAdd(self,left,pas,res,n,stock):
        if left==0:
            res.append(pas)
        else:
            if stock[0] > 0: # (
                stock1 =copy.copy(stock)
                stock1[0]-=1
                self.recurAdd(left-1,pas+"(",res,n,stock1)
            if stock[1] > 0 and stock[0]<stock[1]: # )
                stock1 =copy.copy(stock)
                stock1[1]-=1
                self.recurAdd(left-1,pas+")",res,n,stock1)
        
    def generateParenthesis(self, n: int) -> list[str]:
        rs = []
        self.recurAdd(n*2,"",rs,n*2,[n,n])
        return rs
    
c = Solution()
c.generateParenthesis(3)
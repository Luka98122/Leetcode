class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for char in moves:
            if char == "D":
                y+=1
            if char == "U": 
                y-=1
            if char == "L":
                x-=1
            if char == "R":
                x+=1
        return x==0 and y==0
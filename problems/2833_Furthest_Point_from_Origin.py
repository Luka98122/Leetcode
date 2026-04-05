class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counts = {
            "L" : 0,
            "R" : 0,
            "_" : 0
        }
        
        for char in moves:
            counts[char]+=1
        
        if counts["L"] > counts["R"]:
            return counts["L"]-counts["R"]+counts["_"]
        return counts["R"]-counts["L"]+counts["_"]
        
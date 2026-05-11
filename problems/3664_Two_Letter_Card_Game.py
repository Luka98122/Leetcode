from typing import List
from collections import defaultdict

class Solution: #A
    def score(self, cards: List[str], x: str) -> int:
        hm1 = defaultdict(int)
        hm2 = defaultdict(int)
        wildcards = 0
        
        for card in cards:
            if card == x + x:
                wildcards += 1
            elif card[0] == x:
                hm1[card] += 1
            elif card[1] == x:
                hm2[card] += 1
                
        freqs1 = list(hm1.values())
        sum1 = sum(freqs1)
        max1 = max(freqs1) if freqs1 else 0
        
        freqs2 = list(hm2.values())
        sum2 = sum(freqs2)
        max2 = max(freqs2) if freqs2 else 0
        
        res = 0
        
        for k in range(wildcards + 1):
            curr_sum1 = sum1 + k
            curr_max1 = max(max1, k)
            
            pairs1 = min(curr_sum1 // 2, curr_sum1 - curr_max1)
            
            rem_w = wildcards - k
            curr_sum2 = sum2 + rem_w
            curr_max2 = max(max2, rem_w)
            
            pairs2 = min(curr_sum2 // 2, curr_sum2 - curr_max2)
            
            res = max(res, pairs1 + pairs2)
            
        return res
    
c = Solution()
c.score(["ba","bc","bc","bb","bb","bb"],"b")
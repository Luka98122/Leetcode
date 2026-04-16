class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        if len(timeSeries)==0: return 0
        
        till_when = timeSeries[0]+duration-1
        
        res = duration
        
        for i in range(1,len(timeSeries)):
            if timeSeries[i]<=till_when:
                res+=duration-(till_when-timeSeries[i]+1)
            else:
                res+=duration
            till_when = timeSeries[i]+duration-1
        
        return res
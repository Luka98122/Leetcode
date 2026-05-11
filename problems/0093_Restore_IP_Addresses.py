from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        a = list(s)
        res = set()
        # Try all combos (16^4) and remove duplicates
        for j in range(1,len(s)+1):
            a.insert(j,".")
            for k in range(1,len(s)+2):
                a.insert(k,".")
                for l in range(1,len(s)+3):
                    a.insert(l,".")
                    
                    resStr = "".join(a)
                    
                    ips = resStr.split(".")
                    valid = True
                    for ip in ips:
                        if ip!="":
                            if int(ip)<256:
                                if ip[0]!="0" or (len(ip)==1 and int(ip)==0):
                                    continue
                        valid = False
                    
                    if valid:
                        res.add(resStr)
                    
                    del a[l]
                del a[k]
            del a[j]

        
        return list(res)
    
c = Solution()
print(c.restoreIpAddresses("25525511135"))
                        
                        
            
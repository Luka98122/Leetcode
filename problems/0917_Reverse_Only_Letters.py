import string
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        abc = string.ascii_lowercase + string.ascii_uppercase

        ls = []

        hm = {}
        for i in range(len(s)):
            if s[i] not in abc:
                hm[i] = s[i]
            else:
                ls.append(s[i])
        
        for i in range(len(ls)//2):
            ls[i],ls[len(ls)-1-i] = ls[len(ls)-1-i],ls[i]
        
        for key in hm.keys():
            ls.insert(key,hm[key])

        return "".join(ls)

c = Solution()
print(c.reverseOnlyLetters("abc"))
print(c.reverseOnlyLetters("abcd"))

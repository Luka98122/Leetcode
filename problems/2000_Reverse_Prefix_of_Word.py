class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: return word
        
        ind = word.index(ch)
        
        a = word[0:ind+1]
        a = a[::-1]
        return a+word[ind+1:len(word)]

c = Solution()
print(c.reversePrefix("abcdefd","d"))
        
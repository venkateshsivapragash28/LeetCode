class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        lst = text.split()
        count = 0
        n = len(brokenLetters)
        for i in lst:
            lenth = 0
            for j in brokenLetters:
                if j not in i:
                    lenth += 1
            if lenth == n:
                count += 1
        
        return count
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        dick = {
            'a' : 1,
            'e' : 1,
            'i' : 1,
            'o' : 1,
            'u' : 1
        }
        for i in s:
            if i in dick:
                return True
        return False
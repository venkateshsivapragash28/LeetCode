class Solution:
    def addBinary(self, s: str, b: str) -> str:
        summ = 0
        summm = 0
        s = s[::-1]
        for i in range(len(s)):
            summ += (2**i) * int(s[i])

        b = b[::-1]
        for i in range(len(b)):
            summm += (2**i) * int(b[i])
        
        n = summ + summm
        su = ''
        while n > 1:
            su += str(n%2)
            n = n//2
        su += str(n)

        return su[::-1]
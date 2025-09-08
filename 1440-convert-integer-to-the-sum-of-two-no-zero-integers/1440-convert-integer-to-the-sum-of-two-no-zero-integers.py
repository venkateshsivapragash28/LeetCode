class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        rem = 0
        rem = n % 2
        a = n//2
        if rem:
            b = a + rem
        else:
            b = a
        while str(a).count('0') or str(b).count('0'):
            a -= 1
            b+=1

        return [a,b]        
        
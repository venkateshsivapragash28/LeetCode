class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        summ = 0
        for i in str(x):
            summ += int(i)

        if x % summ == 0:
            return summ
        
        return -1
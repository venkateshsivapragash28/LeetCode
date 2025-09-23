class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = 1
        if num < 0:
            sign = -1
            num = num * sign

        string = ''
        while num > 0:
            mod = num % 7
            num = num // 7
            string += str(mod)

        res = string[::-1]
        if sign == -1:
            res = '-' + res
        return res
class Solution:
    def reverse(self, x: int) -> int:
        sign = '+'
        if str(x)[0] == '-':
            x = int(str(x)[1:])
            sign = '-'
        print(x)
        reverse = 0
        while x:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        
        if sign == '-':
            reverse = reverse * (-1)
        
        if reverse < 2 ** 31 - 1 and reverse > -2**31:
            return reverse
        else:
            return 0
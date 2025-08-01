class Solution(object):
    def myAtoi(self, s):
        
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] == '-':
            s = s[1:]
            sign = -1
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        s = s.lstrip('0')

        num = 0
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            else:
                break
        
        num = num*sign

        int_min = -2**31
        int_max = 2**31 - 1

        if num < int_min:
            return int_min

        elif num > int_max:
            return int_max

        else:
            return num
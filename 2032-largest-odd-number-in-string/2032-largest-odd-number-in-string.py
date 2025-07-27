class Solution(object):
    def largestOddNumber(self, num):
        num = int(num)
        res = ''
        while num > 0:
            if num%2 == 0:
                num = num//10
            else:
                return str(num)
        return ""
                
        

class Solution(object):
    def isHappy(self, n):
        def f(num, seen=set()):
            if num == 1:
                return True
            if num in seen:
                return False
            seen.add(num)
            sum = 0
            num = str(num)
            for i in num:
                sum = sum + int(i)**2
            return f(sum, seen)

        return f(n)

class Solution(object):
    def countAndSay(self, n):
        def f(n, num = '1'):
            if n == 0:
                return num
            new = ''
            count = 1
            for i in range(len(num)-1):
                if num[i] == num[i+1]:
                    count += 1
                else:
                    temp = str(count) + num[i]
                    new = new + temp
                    count = 1
            temp = str(count) + num[-1]
            new = new + temp
            num = new
            return f(n-1, num)
        return f(n-1)
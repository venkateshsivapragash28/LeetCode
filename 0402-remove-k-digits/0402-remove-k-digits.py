class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return '0'
        stack = []
    

        for i in range(len(num)):
            # if stack and stack[-1] <= int(num[i]):
            #     stack.append(int(num[i]))
            while k and stack and stack[-1] > int(num[i]):
                stack.pop()
                k-=1
            stack.append(int(num[i]))
        if k:
            for i in range(k):
                stack.pop()
        res = ''
        for i in stack:
            res = res+ str(i)
        
        while res and res[0] == '0':
            res = res[1:]
        
        if res == '':
            return '0'
        return res
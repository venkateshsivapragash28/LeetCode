class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in s:
            while stack and stack[-1].isdigit() is False and i.isdigit() is True:
                stack.pop()
                break
            else:   
                stack.append(i)
        
        stack = ''.join(stack)
        return stack
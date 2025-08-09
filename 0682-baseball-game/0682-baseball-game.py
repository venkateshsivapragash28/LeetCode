class Solution(object):
    def calPoints(self, ops):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for i in ops:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            if i == '+':
                stack.append(stack[-1] + stack[-2])
            if i == 'D':
                stack.append(stack[-1] * 2)
            if i == 'C':
                stack.pop()
            
        return sum(stack)


        
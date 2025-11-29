class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for i in tokens:
            if i in operators:
                two = stack.pop()
                one = stack.pop()
                if i == '+':
                    stack.append(one + two)
                elif i == '-':
                    stack.append(one - two)
                elif i == '*':
                    stack.append(one * two)
                elif i == '/':
                    stack.append(int(one / two))
            else:
                stack.append(int(i))
        return stack[-1]



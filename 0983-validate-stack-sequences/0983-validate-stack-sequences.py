class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped = popped[::-1]
        stack = []

        if not popped:
            return False

        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[-1]:
                popped.pop()
                stack.pop()

        return True if not stack else False 


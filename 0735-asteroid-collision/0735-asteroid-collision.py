class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack[-1] < abs(asteroids[i]):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])
        return stack


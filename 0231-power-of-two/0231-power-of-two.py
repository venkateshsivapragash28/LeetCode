class Solution(object):
    def isPowerOfTwo(self, n):
        i = 0
        while 2**i<=n:
            if 2**i == n:
                i = i+1
                return True
            else:
                i = i+1
        return False

        
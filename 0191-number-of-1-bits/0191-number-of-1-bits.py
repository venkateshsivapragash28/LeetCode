class Solution:
    def hammingWeight(self, n: int) -> int:
        s = ''
        count = 0
        while n > 1:
            s += str(n%2)
            if n%2 == 1:
                count += 1
            n = n//2
        return count + 1

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        #s = bin(n)[2:]
        return (bin(n)[2:]).count('1')

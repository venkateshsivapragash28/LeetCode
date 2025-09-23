class Solution:
    def minOperations(self, s: str) -> int:
        maxi = 0
        for i in s:
            maxi = max(maxi, (ord('a') - ord(i)) % 26 )
        return maxi
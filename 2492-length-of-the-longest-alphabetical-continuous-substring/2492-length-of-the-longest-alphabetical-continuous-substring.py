class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        count = 1
        max_count = 0
        
        for i in range(len(s)-1):
            if ord(s[i]) + 1 == ord(s[i+1]):
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)

        return max_count
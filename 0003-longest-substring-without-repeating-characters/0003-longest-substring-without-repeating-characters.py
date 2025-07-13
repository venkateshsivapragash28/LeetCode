class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        for i in range(len(s)):
            count = 1
            max_length = max(max_length, count)
            for j in range(i+1, len(s)):
                if s[j] not in s[i:j]:
                    count = count + 1
                    max_length = max(max_length, count)
                else:
                    max_length = max(max_length, count)
                    break
        return max_length



                
    

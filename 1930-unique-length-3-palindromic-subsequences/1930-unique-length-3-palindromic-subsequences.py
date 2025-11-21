class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        
        for c in set(s):
            left = s.find(c)     
            right = s.rfind(c) 
            
            if right > left:
                middle = set(s[left+1:right])
                result += len(middle)
        
        return result
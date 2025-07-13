class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        

        digit = 0
        rev = 0 
        original = x

        while x:
            digit = x%10
            rev = rev*10 + digit
            x = x//10


        if rev == original:    
            return True
        else:
            return False
                
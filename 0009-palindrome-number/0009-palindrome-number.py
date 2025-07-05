class Solution(object):
    def isPalindrome(self, x):
        list = []
        x = str(x)
        for i in x:
            list.append(i)
        result = ''.join(str(i) for i in list)
        result = result[::-1]
        if x == result:
            return True
        else:
            return False

                
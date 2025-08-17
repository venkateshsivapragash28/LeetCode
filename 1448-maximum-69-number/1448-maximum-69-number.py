class Solution:
    def maximum69Number (self, num: int) -> int:
        res = ''
        count = 0
        maxi = 9

        for i in str(num):
            maxi = max(maxi, int(i))

        for i in str(num):
            if count == 0 and i != str(maxi):
                res += str(maxi)
                count+=1
            else:
                res+=i
        
        return int(res)
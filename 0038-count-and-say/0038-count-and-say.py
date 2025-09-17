class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for x in range(n-1):
            count = 1
            res = ''
            for i in range(len(s)-1):
                if s[i] != s[i+1]:
                    res += str(count)
                    res += str(s[i])
                    count = 1
                else:
                    count += 1
                
            res += str(count)
            res += str(s[-1])
            s = res

        return s
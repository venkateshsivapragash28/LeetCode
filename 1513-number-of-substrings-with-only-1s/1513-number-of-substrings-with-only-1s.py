class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        count = 0
        for i in s:
            if i == '0':
                res += (count * (count + 1) ) // 2
                count = 0
            else:
                count += 1

        res += count * (count + 1) //2

        return res % (10**9 + 7)

            
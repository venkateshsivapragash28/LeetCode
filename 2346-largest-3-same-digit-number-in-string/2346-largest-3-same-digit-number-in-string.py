class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # maxi = -1
        # count = 1

        # for i in range(len(num)-1):
        #     if num[i] != num[i+1]:
        #         if count == 3:
        #             maxi = max(maxi, int(num[i]))
        #             count = 1
        #     else:
        #         count+=1
        # if maxi == -1:
        #     return ""
        # else:
        #     return str(maxi)*3

        maxi = -1
        for i in range(len(num)):
            if num[i:i+3].count(num[i:i+3][0]) == 3:
                maxi = max(maxi, int(num[i:i+3][0]))

        if maxi == -1:
            return ""
        else:
            return str(maxi)*3
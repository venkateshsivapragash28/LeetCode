class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s)):
            temp = [0]*26
            for j in range(i, len(s)):
                index = ord(s[j]) - ord('a')
                temp[index] = temp[index] + 1

                max_temp = max(temp)
                min_temp = float('inf')
                for x in temp:
                    if x!= 0:
                        min_temp = min(min_temp, x)
                total = total + (max_temp - min_temp)
        return total

        # 28 - 07 - 2025 ------------------------------------------------
        # total = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         x = s[i:j+1]
        #         if len(x) >= 3:
        #             count = Counter(x)
        #             most = max(count.values())
        #             least = min(count.values())
        #             total = total + (most - least)

        # return total
        
        # ----------------------------------------------------------------


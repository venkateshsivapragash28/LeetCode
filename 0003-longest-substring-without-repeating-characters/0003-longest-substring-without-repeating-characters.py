class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # max_length = 0
        # for i in range(len(s)):
        #     count = 1
        #     max_length = max(max_length, count)
        #     for j in range(i+1, len(s)):
        #         if s[j] not in s[i:j]:
        #             count = count + 1
        #             max_length = max(max_length, count)
        #         else:
        #             max_length = max(max_length, count)
        #             break
        # return max_length


#22-07-2025, second attempt, passed completed

        # string = ''
        # max_count = 0

        # for i in range(len(s)):
        #     string = ''
        #     count = 1
        #     string += s[i]
        #     for j in range(i+1, len(s)):
        #         if s[j] not in string:
        #             count+=1
        #             string+=s[j]
        #             max_count = max(max_count, count)
        #         else:
        #             break
        #     max_count = max(max_count, count)
        # return max_count                
            
# 3rd attempt optmized 13-08-2025 Passed

        # count = 0
        # max_count = 0
        # seen = []
        # i = 0

        # while i < len(s):
        #     if s[i] not in seen:
        #         count+=1
        #         seen.append(s[i])
        #         i+=1
        #     else:
        #         max_count = max(max_count, count)
        #         count = 0
        #         seen = []
        # max_count = max(max_count, count)

        # return max_count

# Revisit revisitted in 01 - 09 - 2025 ---------------------
        left = 0
        right = 0
        dick = set()
        maxi = 0
        while right < len(s):

            if s[right] not in dick:
                dick.add(s[right])
                right+=1        
            elif s[right] in dick:
                while s[right] in dick:
                    dick.remove(s[left])
                    left += 1
            maxi = max(maxi, right - left)
        
        return maxi
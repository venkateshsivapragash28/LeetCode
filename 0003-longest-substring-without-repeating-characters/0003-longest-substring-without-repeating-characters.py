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
            

#Revisit revisitted in 01 - 09 - 2025 ---------------------
        # left = 0
        # right = 0
        # dick = ''
        # maxi = 0
        # while right < len(s):

        #     if s[right] not in dick:
        #         dick += s[right]
        #         right+=1        
        #     elif s[right] in dick:
        #         while s[right] in dick:
        #             dick = dick[1:]
        #             left += 1
        #     maxi = max(maxi, right - left)
        
        # return maxi
        # dick = ''
        # count = 0 
        # maxi = 0
        # for i in s:
        #     if i not in dick:
        #         dick += i
        #         count += 1
        #     else:
        #         while i in dick:
        #             dick = dick[1:]
        #             count -= 1
        #         dick += i
        #         count += 1
        #     maxi = max(maxi, count)
        # return maxi


        maxi = 0
        seen = ''
        count = 0
        for i in s:
            if i not in seen:
                seen += i
                count += 1
            else:
                while i in seen:
                    seen = seen[1:]
                    count -= 1
                seen += i
                count += 1
            maxi = max(maxi, count)
            
        return maxi














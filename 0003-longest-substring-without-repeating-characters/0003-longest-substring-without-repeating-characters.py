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


#22-07-2025, second attempt

        string = ''
        max_count = 0

        for i in range(len(s)):
            string = ''
            count = 1
            string += s[i]
            for j in range(i+1, len(s)):
                if s[j] not in string:
                    count+=1
                    string+=s[j]
                    max_count = max(max_count, count)
                else:
                    break
            max_count = max(max_count, count)
        return max_count                
            

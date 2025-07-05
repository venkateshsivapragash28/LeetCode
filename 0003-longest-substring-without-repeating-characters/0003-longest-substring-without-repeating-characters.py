class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count_list = []
        for i in range(len(s)):
            temp = []
            for j in range(i, len(s)):
                if s[j] not in temp:
                    temp.append(s[j])
                else:
                    break  # break on duplicate
            count_list.append(len(temp))  # always add current length

        return max(count_list) if count_list else 0


                
    

class Solution(object):
    def kthDistinct(self, arr, k):
        counter = {}
        ls = []

        for i in arr:
            if i in counter:
                counter[i] = counter[i]+1
            else:
                counter[i] = 1

        for i in arr:
            if counter[i] == 1:
                ls.append(i)
        if k <= len(ls):
            return ls[k-1]
        else:
            return ""
                
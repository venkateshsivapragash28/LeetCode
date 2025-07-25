class Solution(object):
    def numSmallerByFrequency(self, queries, words):

        # Approach 1 -------- 25 - 07 - 2025
        # def smallest(string):
        #     small = float('inf')
        #     for i in string:
        #         small = min(small, ord(i))
        #     return chr(small)


        # def char_count(string, s):
        #     counter = {}
        #     for i in string:
        #         if i in counter:
        #             counter[i] += 1
        #         else:
        #             counter[i] = 1
        #     return counter.get(s, 0)


        # res = []
        # for i in queries:
        #     count = 0
        #     for j in words:
        #         if char_count(i, smallest(i)) < char_count(j, smallest(j)):
        #             count += 1
        #     res.append(count)
        # return res

        #Approach 2 --------------------- 25 - -7 - 2025
        def smallest(string):
            return min(string)

        def smallest_count(string):
            return string.count(smallest(string))

        q = []
        for i in queries:
            q.append(smallest_count(i))

        w = []
        for i in words:
            w.append(smallest_count(i))

        count = 0
        res = []
        for i in q:
            count = 0
            for j in w:
                if i < j:
                    count+=1
            res.append(count)
        return res
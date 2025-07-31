class Solution(object):
    def groupAnagrams(self, words):
        #31 - 07 - 2025
        # seen = [False]*len(words)
        # final = []

        # for i in range(len(words)):
        #     temp = [words[i]]
        #     if seen[i] == False:
        #         seen[i] = True
        #         for j in range(i+1, len(words)):
        #             if sorted(words[i]) == sorted(words[j]):
        #                 seen[j] = True
        #                 temp.append(words[j])
        #         final.append(temp)

        # return final

        dict = defaultdict(list)

        for word in words:
            key = tuple(sorted(word))
            dict[key].append(word)

        return list(dict.values())

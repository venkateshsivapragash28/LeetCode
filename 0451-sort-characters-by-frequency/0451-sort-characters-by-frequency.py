class Solution:
    def frequencySort(self, s: str) -> str:

        counter = {}
        freq = []
        output = ''

        for i in (s):
            if i in counter:
                counter[i]  = counter[i] + 1
            else:
                counter[i] = 1

        for i in counter:
            freq.append([i, counter[i]])
        freq.sort(key=lambda x: x[1], reverse=True)

        for i in range(len(freq)):
            output = output + freq[i][0]* freq[i][1]

        return output
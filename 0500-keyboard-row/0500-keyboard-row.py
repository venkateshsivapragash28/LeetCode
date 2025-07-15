class Solution(object):
    def findWords(self, words):
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        output = []

        for word in words:
            flag = True
            for char in word:
                if char not in row1:
                    flag = False
                    break
            if flag:
                output.append(word)
                continue

            flag = True
            for char in word:
                if char not in row2:
                    flag = False
                    break
            if flag:
                output.append(word)
                continue

            flag = True
            for char in word:
                if char not in row3:
                    flag = False
                    break
            if flag:
                output.append(word)

        return output

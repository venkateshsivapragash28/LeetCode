class Solution(object):
    def countCharacters(self, words, chars):
        characters = list(chars)
        sample = list(characters)
        total = 0
        count = 0
        for i in words:
            count = 0
            sample = list(characters)
            for j in i:
                if j in sample:
                    sample.remove(j)
                    count+=1
            if count == len(i):
                total = total+count
        return total
        
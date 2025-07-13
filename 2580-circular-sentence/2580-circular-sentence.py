class Solution(object):
    def isCircularSentence(self, sentence):
        arr = sentence.split()
        i = 0
        j = 1
        while i < len(arr) and j < len(arr):
            if arr[i][-1] == arr[j][0]:
                i+=1
                j+=1
            else:
                return False
        if sentence[0][0] == sentence[-1][-1]:
            return True
        else:
            return False
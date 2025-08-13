class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counter1 = {}
        counter2 = {}

        for i in s:
            if i in counter1:
                counter1[i] += 1
            else:
                counter1[i] = 1

        for i in t:
            if i in counter2:
                counter2[i] += 1
            else:
                counter2[i] = 1


        if counter1 == counter2:
            return True
        else:
            return False
class Solution(object):
    def dividePlayers(self, skill):
        half = len(skill)//2
        skill.sort()
        total = 0
        prod = []
        summ = []
        a = skill[ :half]
        b = skill[half:]
        b = b[::-1]
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            prod.append(a[i]*b[j])
            summ.append(a[i]+b[j])
            i+=1
            j+=1
        if len(set(summ)) == 1:
            for i in prod:
                total = total+i
            return total
        else:
            return -1
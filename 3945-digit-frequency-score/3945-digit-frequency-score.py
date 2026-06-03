class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        summ = 0
        seen = {}
        for i in str(n):
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        for i in seen:
            summ += int(i) * seen[i]

        return summ
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        i = 0
        j = 0
        count = {}
        total = 0

        while i < len(fruits) and j < len(fruits):

            if fruits[j] in count:
                count[fruits[j]] += 1
            else:
                count[fruits[j]] = 1

            j += 1

            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]

                i += 1

            total = max(total, j - i)

        return total

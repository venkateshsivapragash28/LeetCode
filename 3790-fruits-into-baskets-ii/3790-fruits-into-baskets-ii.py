class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        for fruit in fruits:
            for basket in baskets:
                if fruit <= basket:
                    baskets.remove(basket)
                    n = n - 1
                    break

        return n
class Solution(object):
    def distributeCandies(self, candyType):
        arr = set(candyType)
        if len(arr) >= len(candyType)/2:
            return len(candyType)/2
        elif len(candyType)/2 > len(arr):
            return len(arr)
        else:
            return 1
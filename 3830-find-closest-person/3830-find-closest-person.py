class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xabs = abs(x - z)
        yabs = abs(y-z)
        if xabs == yabs:
            return 0
        if min(xabs, yabs) == xabs:
            return 1
        elif min(xabs, yabs) == yabs:
            return 2

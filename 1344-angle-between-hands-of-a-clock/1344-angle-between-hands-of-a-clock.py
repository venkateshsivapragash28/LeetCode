class Solution:
    def angleClock(self, hours: int, minutes: int) -> float:
        a = abs((minutes * 6) - (((hours % 12) * 30) + (minutes/2)))
        b = abs(360 - a)
        return min(a,b)
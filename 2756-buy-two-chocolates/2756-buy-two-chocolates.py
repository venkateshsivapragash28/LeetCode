class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()
        if prices[0] + prices[1] <= money:
            return abs((prices[0] + prices[1]) - money)
        else:
            return money
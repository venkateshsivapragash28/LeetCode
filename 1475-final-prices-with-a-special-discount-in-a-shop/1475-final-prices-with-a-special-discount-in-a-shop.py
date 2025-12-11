class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [-1] * len(prices)
        stack = []

        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                top = stack.pop()
                ans[top] = prices[top] - prices[i]
            stack.append(i)

        for i in range(len(prices)):
            if ans[i] == -1:
                ans[i] = prices[i]


        return ans

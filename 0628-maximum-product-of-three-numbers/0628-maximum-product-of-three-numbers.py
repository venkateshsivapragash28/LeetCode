class Solution(object):
    def maximumProduct(self, arr):
        arr.sort()
        product1 = arr[-1]*arr[-2]*arr[-3]
        product2 = arr[0]*arr[1]*arr[-1]

        return max(product1, product2)
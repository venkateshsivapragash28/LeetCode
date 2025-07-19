class Solution(object):
    def generate(self, numRows):
        def pascal(arr):
            res = []
            for i in range(len(arr) - 1):
                res.append(arr[i] + arr[i + 1])
            return [1] + res + [1]

        triangle = [[1]] 
        for i in range(1, numRows):
            next_row = pascal(triangle[-1]) 
            triangle.append(next_row)

        return triangle

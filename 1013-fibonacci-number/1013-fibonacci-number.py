class Solution:
    def fib(self, n: int) -> int:
        def f(n, a, b, arr = None):
            if arr is None:
                arr = [a,b]
            
            if n <= 2:
                return arr
            
            c = a+b
            arr.append(c)

            return f(n-1, b, c, arr)
        if n == 0:
            return 0
        elif n ==1 :
            return 1
        return f(n, 1, 1)[-1]
        
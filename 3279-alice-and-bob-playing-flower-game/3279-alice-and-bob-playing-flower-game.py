class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        def odd(x):
            if x%2 == 1:
                x = x//2
                return x + 1
            else:
                return x//2
            
        def even(x):
            return x//2
                
        return (odd(m)*even(n)) + (even(m) * odd(n))
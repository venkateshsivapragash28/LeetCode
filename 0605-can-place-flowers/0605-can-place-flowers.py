class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] !=1 and flowerbed[i] !=1 and flowerbed[i+1] != 1:
                flowerbed[i] = 1
                n = n-1
        return n<=0

                
                
        
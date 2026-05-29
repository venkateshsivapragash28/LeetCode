class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counter = {}
        ones = []
        twos = []

        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        for key, value in counter.items():
            if value == 1:
                return key
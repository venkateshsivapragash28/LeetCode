class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewels_dict = {}

        for i in jewels:
            if i not in jewels_dict:
                jewels_dict[i] = 1

        count = 0
        for i in stones:
            if i in jewels_dict:
                count += 1

        
        return count

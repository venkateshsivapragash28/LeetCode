class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        occurence = {}
        
        for index, element in enumerate(nums):
            if element in occurence:
                if abs(occurence[element] - index) <= k :
                    return True

            occurence[element] = index
        
        return False

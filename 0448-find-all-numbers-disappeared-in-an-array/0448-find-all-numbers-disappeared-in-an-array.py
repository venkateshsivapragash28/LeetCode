class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        freq = {}
        output = []
        maxi = float('-inf')
        for i in nums:
            if i not in freq:
                freq[i] = 1           
        
        for i in range(1,len(nums)+1):
            if i not in freq:
                output.append(i)

        return output


            

            

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dick = {}
        for i in nums:
            if i in dick:
                dick[i] += 1
            else:
                dick[i] = 1
                
        sorted_items = sorted(dick.items(), key = lambda x: x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])

        return res
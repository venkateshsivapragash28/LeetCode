class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dick = {}

        for word in words:
            if word in dick:
                dick[word] += 1
            else:
                dick[word] = 1

        arr = []
        res = []

        for word, freq in dick.items():
            arr.append((-freq, word))

        heapq.heapify(arr) 

        for _ in range(k):
            res.append(heapq.heappop(arr)[1])


        return res
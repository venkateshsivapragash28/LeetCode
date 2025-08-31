class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        res = []
        def backtrack(index, li):
            if len(li) == k:
                res.append(li[:])
                return
            if index >= n:
                return

            li.append(arr[index])
            backtrack(index + 1, li)
            li.pop()
            backtrack(index + 1, li)

        backtrack(0, [])
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        res = []

        def f(index, li, total):

            if total == target:
                res.append(li[:])
                return

            if index >= n or total > target:
                return

            li.append(candidates[index])
            f(index, li, total + candidates[index])
            li.pop()

            f(index+1, li, total)
        
        f(0, [], 0)

        return res
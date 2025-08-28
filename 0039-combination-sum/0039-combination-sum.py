
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        res = []

        def f(index, li, total):
            # ✅ stop conditions
            if total == target:
                res.append(li[:])
                return
            if index >= n or total > target:
                return

            # ✅ Option 1: pick current number (stay on same index → reuse allowed)
            li.append(candidates[index])
            f(index, li, total + candidates[index])
            li.pop()

            # ✅ Option 2: skip current number (move to next index)
            f(index + 1, li, total)
        
        f(0, [], 0)
        return res

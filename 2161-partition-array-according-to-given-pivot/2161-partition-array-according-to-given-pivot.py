class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s = []
        l = []
        e = []
        for x in nums:
            if x < pivot:
                s.append(x)
            elif x > pivot:
                l.append(x)
            else:
                e.append(x)
        return s + e + l

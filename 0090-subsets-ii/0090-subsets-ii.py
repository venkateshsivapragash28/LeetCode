class Solution:
    def subsetsWithDup(self, li: List[int]) -> List[List[int]]:
        arey = set()
        li.sort()
        for i in range(0, (2 ** len(li))):
            x = bin(i)[2:].zfill(len(li))
            z = []
            for j in range(len(str(x))):
                if x[j] == '1':
                    z.append(li[j])
            arey.add(tuple(z))

        res = []
        for i in arey:
            res.append(list(i))
        return res

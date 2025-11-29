class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        new = []
        output = []
        for i in range(1,n+1):
            if i in target:
                output.append('Push')
                new.append(i)
            else:
                output.append('Push')
                output.append('Pop')

            if new == target:
                return output








        




            




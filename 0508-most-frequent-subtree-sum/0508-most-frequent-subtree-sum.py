# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        dickk = {}
        maxi = 0
        most_freq = []
        def frequentsubtreesum(root):
            nonlocal most_freq
            nonlocal maxi
            if not root:
                return 0

            left = frequentsubtreesum(root.left)
            right = frequentsubtreesum(root.right)

            x = root.val + left + right
            if x in dickk:
                dickk[x] += 1
            else:
                dickk[x] = 1

            if dickk[x] > maxi:
                maxi = dickk[x]
                most_freq = [x]
            elif dickk[x] == maxi:
                most_freq.append(x)
            return x
        
        frequentsubtreesum(root)
        return most_freq
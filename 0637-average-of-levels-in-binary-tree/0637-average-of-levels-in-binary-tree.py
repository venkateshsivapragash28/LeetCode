# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        output = []
        q = [root]
        while  q:
            x = 0
            temp = []
            for node in q:
                x = x + node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            output.append((x/len(q)))
            q = temp
        return output        
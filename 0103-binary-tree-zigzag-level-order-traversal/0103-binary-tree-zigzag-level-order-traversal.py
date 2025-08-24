# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        sign = 0
        output = []
        while q:
            x = []
            temp = []
            for node in q:
                x.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if sign == 1:
                output.append(x[::-1])
            else:
                output.append(x)
            if sign == 0:
                sign = 1
            elif sign == 1:
                sign = 0
            q = temp
        return output
    
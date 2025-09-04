# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = 0
        if not root:
            return 0
        def ff(root, s):
            nonlocal summ
            if root.left:
                ff(root.left, s + str(root.left.val))
            if root.right:
                ff(root.right, s + str(root.right.val))
            elif not root.left and not root.right:
                summ += int(s)

        ff(root, str(root.val))
        return summ
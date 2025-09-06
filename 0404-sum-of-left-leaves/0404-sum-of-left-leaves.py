# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def leftleaves(root):
            nonlocal summ
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                summ+=root.left.val
            leftleaves(root.left)
            leftleaves(root.right)

        leftleaves(root)
        return summ
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def identical(q,p):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if q.val != p.val:
                return False

            left = identical(q.left, p.left)
            if left is False:
                return False

            right = identical(q.right, p.right)
            if right is False:
                return False

            return True

        return identical(p,q)
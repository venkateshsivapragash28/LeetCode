# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def symmetry(a,b):
            if a is None and b is None:
                return True

            if (a is None and b is not None) or (b is None and a is not None):
                return False
            
            if a.val == b.val:
                left = symmetry(a.left, b.right)
                right = symmetry(a.right, b.left)

                return left and right
            else:
                return False
            
        return symmetry(root.left, root.right)
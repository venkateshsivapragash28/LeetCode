# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def f(root, target):
            if not root:
                return
            if root.val == val:
                return root
            
            elif root.val > val:
                return f(root.left, val)
            
            elif root.val < val:
                return f(root.right, val)

            else:
                return None

        return f(root, val)
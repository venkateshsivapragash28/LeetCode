# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        main = root
        def backtrack(root):
            if not root:
                return
            if root.val > val:
                if root.left:
                    backtrack(root.left)
                else:
                    root.left = TreeNode(val)

            elif root.val < val:
                if root.right:
                    backtrack(root.right)
                else:
                    root.right = TreeNode(val)
        backtrack(root)
        return main
            
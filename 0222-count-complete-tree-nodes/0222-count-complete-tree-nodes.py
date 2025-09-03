# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        output = 0
        def backtrack(node):
            nonlocal output
            if not node:
                return
            output+= 1
            backtrack(node.left)
            backtrack(node.right)

        backtrack(root)
        return output
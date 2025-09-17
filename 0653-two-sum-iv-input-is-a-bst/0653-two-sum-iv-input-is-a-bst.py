# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dick = {}
        if not root:
            return
        output = []
        def backtrack(root):
            nonlocal output
            if not root:
                return

            backtrack(root.left)
            output.append(root.val)
            backtrack(root.right)

        backtrack(root)

        for i in output:
            if (k - i) in dick:
                return True
            else:
                dick[i] = 1

        return False
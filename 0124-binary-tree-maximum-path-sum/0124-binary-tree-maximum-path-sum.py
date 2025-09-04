# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #First Try 03 - 09 - 2025

        # max_path = float('-inf')

        # def halfmax(node, t=None):
        #     if not node:
        #         return float('-inf')
        #     if t is None: 
        #         t = node.val
        #     maxi = t
        #     if node.left:
        #         maxi = max(maxi, halfmax(node.left, t + node.left.val))
        #     if node.right:
        #         maxi = max(maxi, halfmax(node.right, t + node.right.val))
        #     return maxi

        # def backtrack(node):
        #     nonlocal max_path
        #     if not node:
        #         return

        #     left_max = halfmax(node.left) if node.left else 0
        #     right_max = halfmax(node.right) if node.right else 0

        #     max_path = max(max_path, left_max + right_max + node.val)

        #     backtrack(node.left)
        #     backtrack(node.right)

        #     return max_path

        # return backtrack(root)

        #Second try 04 - 09 - 2025
        if not root:
            return 0
        maximum = float('-inf')
        def f(root):
            nonlocal maximum

            if not root:
                return 0
            
            left = max(f(root.left), 0)
            right = max(f(root.right), 0)

            maximum = max(maximum, left + right + root.val)

            return root.val + max(left, right)

        f(root)
        return maximum
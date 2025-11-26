# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # def height(root):
        #     if not root:
        #         return 0           
        #     left = height(root.left)
        #     right = height(root.right)
        #     return 1 + max(left, right)    
        # return height(root)
        if not root:
            return 0
        def max_depth(root):
            if not root:
                return 0
            left = max_depth(root.left)
            right = max_depth(root.right)
            return 1 + max(left, right)
        return max_depth(root)
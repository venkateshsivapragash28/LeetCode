# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            return 1 + max(left_height, right_height)

        def isbalanced(node):
            if not node:
                return True

            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                return False
            
            return isbalanced(node.left) and isbalanced(node.right)


        return isbalanced(root)
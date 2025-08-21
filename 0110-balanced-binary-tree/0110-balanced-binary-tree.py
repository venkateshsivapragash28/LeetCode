# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
                return True

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            return 1 + max(left, right)
            

        def balanced(node):
            if not node:
                return True
            
            left = height(node.left)
            right = height(node.right)

            if abs(left - right) > 1:
                return False

            left_balanced = balanced(node.left)
            right_balanced = balanced(node.right)

            if left_balanced and right_balanced:
                return True
            else:
                return False
                
        return balanced(root)
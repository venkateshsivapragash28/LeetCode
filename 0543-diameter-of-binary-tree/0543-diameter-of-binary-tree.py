# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #20 - 08 - 2025
        # def height(node):

        #     if not node:
        #         return 0

        #     else:
        #         left_height = height(node.left)
        #         right_height = height(node.right)

        #         return 1 + max(left_height, right_height)

        # dia = 0

        # def diameter(node):
        #     nonlocal dia
        #     if not node:
        #         return 

        #     left_height = height(node.left) 
        #     right_height = height(node.right)
        #     dia = max(dia, left_height + right_height)

        #     diameter(node.left)
        #     diameter(node.right)
        #     return dia

        # return diameter(root) 

        # 20 - 08 - 2025

        # dia = 0

        # def diameter(node):
        #     nonlocal dia

        #     if not node:
        #         return 0

        #     else:
        #         left_height = diameter(node.left)
        #         right_height = diameter(node.right)

        #         dia = max(dia, left_height + right_height)

        #         return 1 + max(left_height, right_height)

        # diameter(root)
        # return dia

        diameter = 0
        def dia(node):

            nonlocal diameter
            if not node:
                return 0

            else:
                left = dia(node.left)
                right = dia(node.right)
            
            diameter = max(diameter, left + right)

            return 1 + max(left, right)
        
        dia(root)
        return diameter

            

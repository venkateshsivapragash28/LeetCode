# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        
        # def backtrack(root):
        #     if not root:
        #         return 

        #     if root.left:
        #         if root.left.val > root.val:
        #             return False
        #     if root.right:
        #         if root.right.val < root.val:
        #             return False

        #     if backtrack(root.left) and backtracK(root.right):
        #         return True
        #     return False

        # def backtrack(root):
        #     if not root:
        #         return
            
        #     if root.left:
        #         if root.left.val >= root.val:
        #             return False

        #     if root.right:
        #         if root.right.val <= root.val:
        #             return False
                
        #     return True

        #     return backtrack(root.left) and backtrack(root.right)


        # return backtrack(root)
        output = []
        def inorder(root):
            nonlocal output
            if not root:
                return

            inorder(root.left)
            output.append(root.val)
            inorder(root.right)

        inorder(root)

        for i in range(len(output)-1):
            if output[i] >= output[i+1]:
                return False
        return True


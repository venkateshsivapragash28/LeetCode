# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        output = []

        def postorder(root):
            if not root:
                return
            else:
                postorder(root.left)
                postorder(root.right)
                output.append(root.val)
            
        postorder(root)
        return output

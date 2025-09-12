# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        inorder = []
        def backtrack(root):
            if not root:
                return
            
            backtrack(root.left)
            inorder.append(root.val)
            backtrack(root.right)

        backtrack(root)

        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False
        return True
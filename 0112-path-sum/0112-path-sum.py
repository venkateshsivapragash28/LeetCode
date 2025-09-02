# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        stack = [(root, root.val)]

        while stack:
            node, summ = stack.pop()

            if not node.left and not node.right:
                if summ == target:
                    return True
            
            if node.right:
                stack.append((node.right, summ + node.right.val))
            if node.left:
                stack.append((node.left, summ + node.left.val))

        return False
            
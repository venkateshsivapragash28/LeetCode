# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        output = []
        if not root:
            return 0
        q = [root]
        while q:
            x = []
            temp = []
            for node in q:
                x.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                if not node.left and not node.right:
                    return len(output) + 1

            output.append(x)
            q = temp


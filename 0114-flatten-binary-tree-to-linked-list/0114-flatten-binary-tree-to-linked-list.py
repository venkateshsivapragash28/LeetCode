# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        def PreOrder(node):
            nonlocal nodes
            if not node:
                return
            else:
                nodes.append(node)
                PreOrder(node.left)
                PreOrder(node.right)
            return nodes
        
        PreOrder(root)

        for i in range(1,len(nodes)):
            prev, curr = nodes[i-1], nodes[i]
            prev.left = None
            prev.right = curr
            
        

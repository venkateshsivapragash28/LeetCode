# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 
        output = []
        q = [root]

        while  q:   
            even = float('inf')
            odd = float('-inf')

            x = []
            temp = []
            for node in q:
                x.append(node.val)
                if len(output) % 2 == 0:
                    if node.val % 2 == 0 or node.val <= odd:
                        return False
                    odd = node.val
                if len(output) % 2 == 1:    
                    if node.val % 2 == 1 or node.val >= even:
                        return False
                    even = node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            output.append(x)
            q = temp
        return True
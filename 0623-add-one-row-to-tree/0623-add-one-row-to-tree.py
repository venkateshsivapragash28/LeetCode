# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node


        q = [root]
        res = []
        while q and len(res) < depth:
            x = []
            temp = []
            for node in q:
                x.append(node)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(x)
            q = temp

        for n in res[depth-2]:
            if n.left:
                new_node = TreeNode(val)
                new_node.left = n.left
                n.left = new_node
            else: 
                n.left = TreeNode(val)

            if n.right:
                new_node = TreeNode(val)
                new_node.right = n.right
                n.right = new_node
            else:  
                n.right = TreeNode(val)

        return root
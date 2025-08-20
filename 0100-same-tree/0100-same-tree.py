# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if (not p) and (not q):
        #     return True
        # if (not p) or (not q):
        #     return False
        
        # if(self.isSameTree(p.left, q.left) == False):
        #     return False
        # if p.val != q.val:
        #     return False
        # if(self.isSameTree(p.right, q.right) == False):
        #     return False 
        # if p.val != q.val:
        #     return False
        
        # return True
        # return (not p and not q) or (p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)); 
        # print(str(p)); 
        return str(p) == str(q); 
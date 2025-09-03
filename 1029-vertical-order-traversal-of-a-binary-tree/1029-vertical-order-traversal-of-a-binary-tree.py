# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = {}
        q = [(root, 0, 0)]
        while q:
            node, vertical, row = q.pop(0)
            if vertical not in output:
                output[vertical] = []
            output[vertical].append((node.val, row))

            if node.left:
                q.append((node.left, vertical - 1, row + 1))

            if node.right:
                q.append((node.right, vertical + 1, row + 1))

        p = []
        for i in sorted(output):
            output[i].sort(key = lambda x: (x[1], x[0]))
            temp = []
            for val, row in output[i]:
                temp.append(val)
            p.append(temp)

        return p
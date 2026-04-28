# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        cur = root
        stack = []
        res = []

        while cur or stack:
            if cur:
                stack.append(cur.right)
                res.append(cur.val)
                cur = cur.left
            elif stack:
                cur = stack.pop()
        return res
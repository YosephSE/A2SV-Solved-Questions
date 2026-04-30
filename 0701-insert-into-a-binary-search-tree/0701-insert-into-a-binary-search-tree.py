# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        
        def search(node, val):
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    search(node.left, val)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    search(node.right, val)
        
        search(root, val)
        return root
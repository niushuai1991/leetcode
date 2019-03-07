# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check(node, min_val, max_val):
            if node is None:
                return True
            if (min_val is None or node.val < min_val) and (max_val is None or node.val > max_val):
                return check(node.left, node.val, max_val) and check(node.right, min_val, node.val)
            else:
                return False
        return check(root, None, None)

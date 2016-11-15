# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            left = root.left
            root.left = root.right
            root.right = left
            if root.left:
                Solution().invertTree(root.left)
            if root.right:
                Solution().invertTree(root.right)
            
        return root

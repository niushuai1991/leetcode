# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        基于BFS算法实现
        """
        if not root:
            return None
        queue = list()
        queue.append(root)
        while len(queue) != 0:
            current = queue.pop()
            current.left, current.right = current.right, current.left
            if (current.left != None):
                queue.append(current.left)
            if (current.right != None):
                queue.append(current.right)
        return root
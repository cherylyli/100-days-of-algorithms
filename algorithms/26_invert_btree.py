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
        if not root:
            return
        
        # if is leaf
        if not root.left and not root.right:
            return root
        
        new_right = self.invertTree(root.left)
        new_left = self.invertTree(root.right)
        new_node = TreeNode(root.val)
        new_node.left = new_left
        new_node.right = new_right
        return new_node
        
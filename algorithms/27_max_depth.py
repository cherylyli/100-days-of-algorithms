# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # if root is empty
        if not root:
            return 0
            
        # if root is a leaf
        if not root.left and not root.right:
            return 1
            
        # otherwise, return max height of left or right tree plus 1
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
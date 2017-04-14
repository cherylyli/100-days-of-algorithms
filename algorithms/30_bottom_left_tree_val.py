# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_left(root, levels, level):
            """
            find leftmost element of each row
            """
            if len(levels) <= level:
                levels.append(root.val)
            if root.left:
                find_left(root.left, levels, level+1)
            if root.right:
                find_left(root.right, levels, level+1)
            return levels
        
        return find_left(root, [], 0)[-1]
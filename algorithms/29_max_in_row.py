# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def flatten(root, levels, level):
            """
            find the nums in a given level
            """
            if len(levels)<=level:
                levels.append(root.val)
            elif root.val > levels[level]:
                levels[level] = root.val
            
            if root.left:
                flatten(root.left, levels, level+1)
            if root.right:
                flatten(root.right, levels, level+1)
            return levels

        if not root:
            return []
        levels = flatten(root, [], 0)
        return levels
            
        
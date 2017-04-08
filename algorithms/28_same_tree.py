# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # if neither exist or only one doesn't exist
        if not p or not q:
            if not p and not q:
                return True
            else:
                return False
                
        # if values not same, return False
        if p.val != q.val:
            return False
            
        # if both are leaves:
        if (not p.left and not p.right) or (not q.left and not q.right):
            if (not p.left and not p.right) and (not q.left and not q.right):
                return True
            else:
                return False
                
        
        # else, check if left & right branches are same
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        
        if left_same and right_same:
            return True
        return False
        
        
        
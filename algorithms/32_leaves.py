# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def findLeaves(root):
            """
            given a root, find the leaves
            """
            leaves = []
            if not root:
                return None, leaves
            
            # if root is a leaf
            if not root.left and not root.right:
                leaves.append(root.val)
                root = None
                return None, leaves
                
            # if root is not a leave, find the leaf
            if root.left:
                root.left, new_left =  findLeaves(root.left)
                leaves += new_left
            if root.right:
                root.right, new_right =  findLeaves(root.right)
                leaves += new_right
            
            return root, leaves
            
            
        leave_layers = []
        
        # while root is not None
        while root:
            # get leaves, append to leave_layers
            root, leaves = findLeaves(root)
            leave_layers.append(leaves)
            
            
        return leave_layers